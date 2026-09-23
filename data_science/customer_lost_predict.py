
"""
项目需求：完成端到端建模全流程
数据加载 → 探索性分析EDA → 数据预处理 → 特征工程 → 逻辑回归/随机森林建模 → 模型评估 → 结果对比
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, precision_score, recall_score

#模拟电信客户流失数据
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    "客户ID": range(1, n+1),
    "月费": np.random.uniform(30, 150, n),
    "入网月数": np.random.randint(1, 60, n),
    "客服呼叫次数": np.random.poisson(2, n),
    "是否合约用户": np.random.choice(["是", "否"], n, p=[0.4, 0.6]),
    "性别": np.random.choice(["男", "女"], n)
})

#特征工程
p_churn = (data["月费"] - 30) / 120 * 0.5 + 0.2     # 月费高→流失概率高
p_churn += (60 - data["入网月数"]) / 60 * 0.3        # 入网月数越低越容易流失
p_churn += data["客服呼叫次数"] * 0.05               # 客服呼叫次数越多越容易流失
p_churn += (data["是否合约用户"] == "否") * 0.2      # 非合约用户更容易流失
p_churn = np.clip(p_churn, 0, 1)                    # 限制在0-1之间
# print(p_churn)

data["是否流失"] = np.random.binomial(1, p_churn)   # 根据概率生成标签

#提取特征和标签
X = data.drop(["是否流失", "客户ID"], axis=1)
y = data["是否流失"]
# print(X.head())
# print(y.head())

#===== 1. 划分数据集 =====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# print(X_train[:10])

#===== 2.预处理Pipeline =====
num_col = ["月费", "入网月数", "客服呼叫次数"]
cat_col = ["是否合约用户", "性别"]

#标准化
# scaler = StandardScaler()
# scaler.fit_transform(X_train[num_col])

#独热编码
# onehot = OneHotEncoder(drop="first")
# onehot.fit_transform(X_train[["是否合约用户"]])

#标签编码
# label = LabelEncoder()
# y = label.fit_transform(X_train["性别"])
# print(y[:10])

col_preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_col),
    ("cat", OneHotEncoder(drop="first"), ["是否合约用户", "性别"])  #需要带[]（二维数组）
])                                                                          
# col_preprocessor.fit_transform(X_train)         #标签编码的fit_transform只接受1个入参      

#===== 3. 构建两个模型流水线 =====
#逻辑回归模型
pipeline_log = Pipeline([
    ("preprocess", col_preprocessor),
    ("model", LogisticRegression(random_state=42))
])

#随机森林模型
pipeline_rand = Pipeline([
    ("preprocess", col_preprocessor),
    ("model", RandomForestClassifier(n_estimators=100, random_state=42))
])

#===== 4. 训练与评估 =====
def evaluate_model(pipeline, X_train, X_test, y_train, y_test, name):
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, 1]      #样本属于正例的概率

    # print(np.unique(y_pred, return_counts=True))
    # print(sum((y_proba >= 0.5).astype(int)))

    print(f"===== {name} 评估结果 =====")
    print(f"准确率：{accuracy_score(y_test, y_pred):.4f}")
    print(f"精确率：{precision_score(y_test, y_pred):.4f}")   #数据是随机的，模型学不到任何规律，所以精确率0
    print(f"召回率：{recall_score(y_test, y_pred):.4f}")
    print(f"f1分数：{f1_score(y_test, y_pred):.4f}")
    print(f"AUC指标：{roc_auc_score(y_test, y_proba):.4f}")
    return pipeline

model_log = evaluate_model(pipeline_log, X_train, X_test, y_train, y_test, "逻辑回归模型")
model_rand = evaluate_model(pipeline_rand, X_train, X_test, y_train, y_test, "随机森林模型")

#===== 5. 特征重要性分析（随机森林）=====
feature_names = num_col + list(pipeline_rand.named_steps["preprocess"].named_transformers_["cat"].get_feature_names_out())
# print(feature_names)

importances = model_rand.named_steps["model"].feature_importances_
# print(importances)

feat_imp = pd.DataFrame({
    "特征": feature_names,
    "重要性": importances
}).sort_values("重要性", ascending=False)

print(feat_imp)