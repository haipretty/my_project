
import random

def create_nums() -> list:
    """生成中奖号码"""
    nums = []
    while len(nums) < 6:                    #6个红球号码
        red_num = random.randint(1, 33)     #生成红球号码
        if red_num not in nums:
            nums.append(red_num)            #不重复时添加到列表
    nums.sort()                             #排序
    blue_num = random.randint(1, 16)        #生成蓝球号码
    nums.append(blue_num)                   #添加蓝球号码
    return nums

def is_winned(win_nums:list, buy_nums:list) -> None:
    """查看是否中奖"""
    buy_nums_reds = buy_nums[:-1]
    buy_nums_blue = buy_nums[-1]
    win_nums_reds = win_nums[:-1]
    win_nums_blue = win_nums[-1]
    
    red = 0
    blue = 0
    for buy in buy_nums_reds:               #判断中的红色球个数
        if buy in win_nums_reds:
            red += 1
    if buy_nums_blue == win_nums_blue:      #判断中的蓝色球个数
        blue += 1
    
    print(win_nums)                 #打印中将号码
    print(buy_nums)                 #打印购买号码

    if red == 6 and blue == 1:
        print("==恭喜您，中了一等奖！==")
    elif red == 6:
        print("==恭喜您，中了二等奖！==")
    elif red == 5 and blue == 1:
        print("==恭喜您，中了三等奖！==")
    elif red == 5 or (red == 4 and blue == 1):
        print("==恭喜您，中了四等奖！==")
    elif red == 4 or (red ==3 and blue == 1):
        print("==恭喜您，中了五等奖！==")
    elif blue == 1:
        print("==恭喜您，中了六等奖！==")
    else:
        print("很遗憾，您未中奖。")
        print(f"您猜中了 {red} 个红球，{blue} 个蓝球.")
    
    return

if __name__ == "__main__":
    buy_nums = [6,7,19,20,22,33,8]
    for i in range(10):
        win_nums = create_nums()     
        is_winned(win_nums, buy_nums)
        print("\n")