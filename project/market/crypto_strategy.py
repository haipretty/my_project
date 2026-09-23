import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import warnings
warnings.filterwarnings('ignore')

class CryptoOpenStrategyBacktest:
    """
    加密货币开放赛道 - 趋势跟踪策略回测框架

    策略逻辑：
    1. 大盘择时：BTC 价格在 20 周期均线上方，且均线向上 → 重仓(80%)
                  否则 → 轻仓(30%) 或空仓
    2. 动量选股：选 20 周期涨幅排名前 N 的币，且价格站上短期均线
    3. 硬风控：单币亏损 -8% 止损；总账户回撤 -15% 清仓观望
    4. 再平衡：按设定频率检查调仓（默认每 24 个周期，约每天一次）
    """

    def __init__(self, symbols, timeframe='1h', start_days_ago=180,
                 initial_capital=10000, top_n=5, commission=0.001,
                 rebalance_freq=24):
        self.exchange = ccxt.binance({
            'enableRateLimit': True,
            'options': {'defaultType': 'spot'}
        })
        self.symbols = symbols
        self.timeframe = timeframe
        self.initial_capital = initial_capital
        self.top_n = top_n
        self.commission = commission
        self.rebalance_freq = rebalance_freq  # 每 N 个周期调仓一次

        # 策略参数
        self.ma_short = 20
        self.ma_long = 60
        self.mom_period = 20
        self.stop_loss = 0.08
        self.max_dd_limit = 0.15
        self.high_pos = 0.8
        self.low_pos = 0.3

        # 数据存储
        self.data = {}
        self.btc_data = None
        self.equity_curve = None
        self.records = None

    # ==================== 数据获取 ====================
    def fetch_data(self, symbol, since=None):
        """分页获取 K 线数据（自动处理币安 API 限制）"""
        all_ohlcv = []
        limit = 1000

        if since is None:
            since = self.exchange.parse8601(
                (datetime.utcnow() - timedelta(days=180)).isoformat()
            )

        while True:
            try:
                ohlcv = self.exchange.fetch_ohlcv(
                    symbol, timeframe=self.timeframe, since=since, limit=limit
                )
                if not ohlcv:
                    break
                all_ohlcv.extend(ohlcv)
                since = ohlcv[-1][0] + 1

                if len(ohlcv) < limit:
                    break
                time.sleep(self.exchange.rateLimit / 1000)

            except Exception as e:
                print(f"  ⚠️ 获取 {symbol} 出错: {e}")
                time.sleep(2)
                break

        df = pd.DataFrame(all_ohlcv, 
                          columns=['timestamp','open','high','low','close','volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        df = df[~df.index.duplicated(keep='first')]
        return df.sort_index()

    def fetch_all_data(self):
        """批量获取所有标的"""
        print("=" * 60)
        print("📡 开始获取数据...")
        for symbol in self.symbols:
            print(f"  正在获取 {symbol} ...", end=" ")
            df = self.fetch_data(symbol)
            min_required = self.ma_long + self.mom_period + 10
            if len(df) > min_required:
                self.data[symbol] = df
                print(f"✅ {len(df)} 条 | {df.index[0].date()} ~ {df.index[-1].date()}")
            else:
                print(f"❌ 数据不足 ({len(df)} 条)，已跳过")
        if 'BTC/USDT' in self.data:
            self.btc_data = self.data['BTC/USDT'].copy()
        print(f"📊 成功加载 {len(self.data)} 个标的")
        print("=" * 60)

    # ==================== 信号计算 ====================
    def calculate_signals(self):
        """计算技术指标"""
        print("🔧 计算技术指标...")
        for symbol, df in self.data.items():
            df['ma_s'] = df['close'].rolling(self.ma_short).mean()
            df['ma_l'] = df['close'].rolling(self.ma_long).mean()
            df['momentum'] = df['close'] / df['close'].shift(self.mom_period) - 1
            self.data[symbol] = df

        if self.btc_data is not None:
            self.btc_data['ma_s'] = self.btc_data['close'].rolling(self.ma_short).mean()
            self.btc_data['ma_l'] = self.btc_data['close'].rolling(self.ma_long).mean()
            self.btc_data['trend_bull'] = (
                (self.btc_data['close'] > self.btc_data['ma_s']) & 
                (self.btc_data['ma_s'] > self.btc_data['ma_l'])
            ).astype(int)
        print("✅ 信号计算完成")

    # ==================== 回测引擎 ====================
    def backtest(self):
        """事件驱动回测主循环"""
        print("🚀 开始回测...")

        all_idx = None
        for df in self.data.values():
            all_idx = df.index if all_idx is None else all_idx.union(df.index)
        all_idx = all_idx.sort_values()

        signal_df = pd.DataFrame(index=all_idx)
        signal_df['btc_trend'] = 0
        if self.btc_data is not None:
            signal_df.loc[self.btc_data.index, 'btc_trend'] = self.btc_data['trend_bull']

        for sym in self.data.keys():
            df = self.data[sym]
            signal_df[f'{sym}_close'] = df['close']
            signal_df[f'{sym}_mom'] = df['momentum']
            signal_df[f'{sym}_ma_s'] = df['ma_s']

        signal_df = signal_df.ffill()
        valid_start = max([df.index[self.ma_long + self.mom_period] for df in self.data.values()])
        signal_df = signal_df[signal_df.index >= valid_start]

        capital = self.initial_capital
        equity_curve = [capital]
        timestamps = [signal_df.index[0]]
        positions = {}
        symbols = list(self.data.keys())

        for i, (ts, row) in enumerate(signal_df.iterrows()):
            if i == 0: continue

            btc_bull = int(row['btc_trend']) == 1
            target_ratio = self.high_pos if btc_bull else self.low_pos

            candidates = {}
            for sym in symbols:
                c, m, ma = f'{sym}_close', f'{sym}_mom', f'{sym}_ma_s'
                if c not in row or pd.isna(row[c]) or pd.isna(row[m]): continue
                if ma in row and pd.notna(row[ma]) and row[c] > row[ma]:
                    candidates[sym] = row[m]

            selected = set()
            if len(candidates) >= self.top_n:
                selected = set(sorted(candidates, key=candidates.get, reverse=True)[:self.top_n])

            port_val = capital
            for sym, pos in positions.items():
                c = f'{sym}_close'
                if c in row and pd.notna(row[c]):
                    port_val += pos['shares'] * row[c]

            tgt_per = (port_val * target_ratio) / len(selected) if selected else 0

            to_sell = set()
            for sym, pos in positions.items():
                c = f'{sym}_close'
                if c not in row or pd.isna(row[c]): continue
                price = row[c]
                if price > pos['high']: pos['high'] = price
                if (price - pos['entry']) / pos['entry'] < -self.stop_loss:
                    to_sell.add(sym); continue
                if sym not in selected: to_sell.add(sym)

            for sym in to_sell:
                c = f'{sym}_close'
                if c in row and pd.notna(row[c]):
                    capital += positions[sym]['shares'] * row[c] * (1 - self.commission)
                    del positions[sym]

            if i % self.rebalance_freq == 0:
                for sym in selected:
                    c = f'{sym}_close'
                    if c not in row or pd.isna(row[c]): continue
                    price = row[c]
                    if sym in positions:
                        cur_val = positions[sym]['shares'] * price
                        if abs(cur_val - tgt_per) / tgt_per > 0.25 and tgt_per > 0:
                            capital += positions[sym]['shares'] * price * (1 - self.commission)
                            del positions[sym]
                            buy_p = price * (1 + self.commission)
                            shares = int(tgt_per / buy_p * 10000) / 10000
                            if shares > 0 and capital >= shares * buy_p:
                                capital -= shares * buy_p
                                positions[sym] = {'entry': buy_p, 'shares': shares, 'high': buy_p}
                    else:
                        buy_p = price * (1 + self.commission)
                        shares = int(tgt_per / buy_p * 10000) / 10000
                        if shares > 0 and capital >= shares * buy_p:
                            capital -= shares * buy_p
                            positions[sym] = {'entry': buy_p, 'shares': shares, 'high': buy_p}

            cur_eq = capital
            for sym, pos in positions.items():
                c = f'{sym}_close'
                if c in row and pd.notna(row[c]):
                    cur_eq += pos['shares'] * row[c]

            peak = max(equity_curve)
            if peak > 0 and (peak - cur_eq) / peak > self.max_dd_limit:
                for sym, pos in list(positions.items()):
                    c = f'{sym}_close'
                    if c in row and pd.notna(row[c]):
                        capital += pos['shares'] * row[c] * (1 - self.commission)
                positions.clear()
                cur_eq = capital

            equity_curve.append(cur_eq)
            timestamps.append(ts)

        self.equity_curve = pd.Series(equity_curve, index=timestamps)
        print("✅ 回测完成")
        return self.equity_curve

    # ==================== 绩效评估 ====================
    def evaluate(self):
        """计算比赛所需全部指标"""
        eq = self.equity_curve
        ret = eq.pct_change().dropna()

        total_ret = (eq.iloc[-1] - self.initial_capital) / self.initial_capital
        days = (eq.index[-1] - eq.index[0]).total_seconds() / 86400
        ann_ret = (1 + total_ret) ** (365 / days) - 1 if days > 0 else 0

        cummax = eq.cummax()
        dd = (eq - cummax) / cummax
        max_dd = dd.min()

        if self.timeframe == '1m':
            periods_per_year = 365 * 24 * 60
        elif self.timeframe == '1h':
            periods_per_year = 365 * 24
        elif self.timeframe == '4h':
            periods_per_year = 365 * 6
        else:
            periods_per_year = 365

        sharpe = (ret.mean() / ret.std() * np.sqrt(periods_per_year)) if ret.std() > 0 else 0
        win_rate = (ret > 0).mean()

        print("\n" + "=" * 60)
        print("📊 策略绩效报告（加密货币开放赛道）")
        print("=" * 60)
        print(f"回测区间      : {eq.index[0]} ~ {eq.index[-1]}")
        print(f"K线周期       : {self.timeframe}")
        print(f"总周期数      : {len(eq):,}")
        print(f"初始资金      : ${self.initial_capital:,.2f}")
        print(f"最终权益      : ${eq.iloc[-1]:,.2f}")
        print(f"总收益率      : {total_ret*100:+.2f}%")
        print(f"年化收益率    : {ann_ret*100:+.2f}%")
        print(f"最大回撤      : {max_dd*100:.2f}%")
        print(f"夏普比率      : {sharpe:.2f}")
        print(f"日胜率        : {win_rate*100:.1f}%")
        print("=" * 60)

        print("\n🎯 比赛门槛检查")
        if max_dd > -0.25:
            print(f"   ✅ 开放赛道门槛通过（回撤 {max_dd*100:.2f}% < -25%）")
        else:
            print(f"   ❌ 未通过！回撤 {max_dd*100:.2f}% 超出 -25% 限制")

        self._plot(eq, dd)

        return {
            'total_return': total_ret,
            'annual_return': ann_ret,
            'max_drawdown': max_dd,
            'sharpe_ratio': sharpe,
            'win_rate': win_rate
        }

    def _plot(self, eq, dd):
        """绘制权益曲线与回撤"""
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), 
                                        gridspec_kw={'height_ratios': [3, 1]})

        ax1.plot(eq.index, eq.values, color='#2E86AB', lw=1.2, label='Portfolio Value')
        ax1.axhline(self.initial_capital, color='gray', ls='--', alpha=0.5)
        ax1.set_title('Crypto Open Strategy Backtest', fontsize=14)
        ax1.set_ylabel('USDT')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ax2.fill_between(dd.index, dd.values*100, 0, color='#E94F37', alpha=0.5)
        ax2.axhline(-25, color='red', ls='--', alpha=0.7, label='Open Track Limit (-25%)')
        ax2.axhline(-15, color='orange', ls='--', alpha=0.7, label='Strategy Cut (-15%)')
        ax2.set_ylabel('Drawdown %')
        ax2.set_xlabel('Date')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('/mnt/agents/output/backtest_chart.png', dpi=150, bbox_inches='tight')
        print("\n📈 图表已保存: /mnt/agents/output/backtest_chart.png")
        plt.show()


# ==================== 运行入口 ====================
if __name__ == "__main__":
    SYMBOLS = [
        'BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT',
        'XRP/USDT', 'DOGE/USDT', 'ADA/USDT', 'AVAX/USDT',
        'LINK/USDT', 'DOT/USDT', 'MATIC/USDT', 'LTC/USDT'
    ]

    bt = CryptoOpenStrategyBacktest(
        symbols=SYMBOLS,
        timeframe='1h',          # 测试用 '1h'，正式提交前改为 '1m'
        initial_capital=10000,
        top_n=5,
        commission=0.001,
        rebalance_freq=24
    )

    bt.fetch_all_data()
    bt.calculate_signals()
    bt.backtest()
    bt.evaluate()