**机器学习专项练习题（含参考答案）**

**前言**

本文档匹配计划学习机器学习的朋友，涵盖**Sklearn环境配置、数据预处理、回归/分类建模、集成学习、聚类算法、模型评估、超参数调优**。所有题目均提供了可直接执行的初始化代码和参考答案，建议先独立完成题目，再核对代码。

**通用前置环境配置**

所有练习题基于Python + Scikit-learn生态，执行前请先安装依赖并导入基础库。

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# 安装依赖（命令行执行）<br />
# pip install numpy pandas scikit-learn matplotlib seaborn<br />
<br />
import numpy as np<br />
import pandas as pd<br />
import matplotlib.pyplot as plt<br />
import seaborn as sns<br />
<br />
# 全局配置<br />
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']<br />
plt.rcParams['axes.unicode_minus'] = False<br />
np.random.seed(2026) # 保证结果可复现</td>
</tr>
</tbody>
</table>

**一、基础概念与环境准备（第46天）**

**对应知识点：机器学习分类、Sklearn安装、数据集加载、训练集划分**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import load_iris<br />
from sklearn.model_selection import train_test_split</td>
</tr>
</tbody>
</table>

**题目列表**

|      |            |                                                                                             |
|------|------------|---------------------------------------------------------------------------------------------|
| 题号 | 题目类型   | 需求描述                                                                                    |
| 1    | 概念辨析   | 分别列举3个监督学习场景和3个无监督学习场景，并说明判断依据                                  |
| 2    | 环境验证   | 加载sklearn内置鸢尾花数据集，输出特征名称、标签名称、数据维度                               |
| 3    | 数据集划分 | 将鸢尾花数据集按7:3比例划分为训练集和测试集，设置随机种子为42，输出训练集、测试集的样本数量 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：概念辨析 ----------<br />
# 监督学习（有标签y）：房价预测、垃圾邮件分类、客户流失预测<br />
# 无监督学习（无标签y）：用户分群、异常检测、商品关联规则挖掘<br />
#
判断依据：训练数据是否包含明确的「目标标签/结果」，模型需要学习特征到标签的映射<br />
<br />
# ---------- 题2：加载数据集 ----------<br />
iris = load_iris()<br />
print("特征名称：", iris.feature_names)<br />
print("标签名称：", iris.target_names)<br />
print("数据维度：", iris.data.shape) # 150个样本，4个特征<br />
<br />
# ---------- 题3：划分训练集测试集 ----------<br />
X = iris.data<br />
y = iris.target<br />
X_train, X_test, y_train, y_test = train_test_split(<br />
X, y, test_size=0.3, random_state=42<br />
)<br />
print(f"训练集样本数：{X_train.shape[0]}")<br />
print(f"测试集样本数：{X_test.shape[0]}")</td>
</tr>
</tbody>
</table>

**二、数据预处理与特征工程（第47天）**

**对应知识点：缺失值处理、标准化、归一化、分类编码、Pipeline流水线**

**初始化代码（生成模拟数据）**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.preprocessing import StandardScaler, MinMaxScaler,
OneHotEncoder, LabelEncoder<br />
from sklearn.impute import SimpleImputer<br />
from sklearn.pipeline import Pipeline<br />
from sklearn.compose import ColumnTransformer<br />
<br />
# 生成带缺失值、分类特征的模拟用户数据<br />
data = pd.DataFrame({<br />
"年龄": [25, 30, np.nan, 45, 35, 28, 50, np.nan, 32, 40],<br />
"收入": [5000, 8000, 6500, 12000, 9000, np.nan, 15000, 7000, 8500,
11000],<br />
"性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男",
"女"],<br />
"城市": ["北京", "上海", "广州", "深圳", "北京", "上海", "广州", "深圳",
"北京", "上海"],<br />
"是否流失": [0, 0, 1, 0, 1, 0, 0, 1, 0, 1]<br />
})<br />
X = data.drop("是否流失", axis=1)<br />
y = data["是否流失"]</td>
</tr>
</tbody>
</table>

**题目列表**

|      |                |                                                                   |
|------|----------------|-------------------------------------------------------------------|
| 题号 | 题目类型       | 需求描述                                                          |
| 1    | 缺失值处理     | 对数值列「年龄、收入」用均值填充缺失值，输出填充后的数据          |
| 2    | 分类编码       | 对「性别」做标签编码，对「城市」做独热编码，输出转换后的数据      |
| 3    | 数值缩放       | 对填充后的数值列分别做标准化和最小最大归一化，对比两者结果差异    |
| 4    | Pipeline流水线 | 构建完整预处理Pipeline：数值列自动填充+标准化，分类列自动独热编码 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：缺失值填充 ----------<br />
num_cols = ["年龄", "收入"]<br />
imputer = SimpleImputer(strategy="mean")<br />
X[num_cols] = imputer.fit_transform(X[num_cols])<br />
print("缺失值填充后：")<br />
print(X[num_cols])<br />
<br />
# ---------- 题2：分类编码 ----------<br />
# 标签编码<br />
le = LabelEncoder()<br />
X["性别_编码"] = le.fit_transform(X["性别"])<br />
<br />
# 独热编码<br />
encoder = OneHotEncoder(sparse_output=False, drop="first")<br />
city_encoded = encoder.fit_transform(X[["城市"]])<br />
city_df = pd.DataFrame(city_encoded,
columns=encoder.get_feature_names_out(["城市"]))<br />
X_encoded = pd.concat([X.reset_index(drop=True), city_df], axis=1)<br />
print("\n分类编码后：")<br />
print(X_encoded)<br />
<br />
# ---------- 题3：数值缩放 ----------<br />
# 标准化：均值0，方差1<br />
scaler_std = StandardScaler()<br />
X_std = scaler_std.fit_transform(X[num_cols])<br />
<br />
# 归一化：压缩到[0,1]区间<br />
scaler_minmax = MinMaxScaler()<br />
X_minmax = scaler_minmax.fit_transform(X[num_cols])<br />
<br />
print("标准化结果前3行：\n", X_std[:3])<br />
print("归一化结果前3行：\n", X_minmax[:3])<br />
<br />
# ---------- 题4：预处理Pipeline ----------<br />
num_pipeline = Pipeline([<br />
("imputer", SimpleImputer(strategy="mean")),<br />
("scaler", StandardScaler())<br />
])<br />
<br />
full_pipeline = ColumnTransformer([<br />
("num", num_pipeline, num_cols),<br />
("cat", OneHotEncoder(drop="first"), ["性别", "城市"])<br />
])<br />
<br />
X_processed = full_pipeline.fit_transform(X)<br />
print("\nPipeline处理后数据维度：", X_processed.shape)</td>
</tr>
</tbody>
</table>

**三、线性回归与回归评估（第48天）**

**对应知识点：线性回归建模、MSE/RMSE/R²评估、特征系数解释**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import fetch_california_housing<br />
from sklearn.linear_model import LinearRegression<br />
from sklearn.metrics import mean_squared_error, r2_score<br />
from sklearn.model_selection import train_test_split<br />
from sklearn.preprocessing import StandardScaler<br />
<br />
# 加载加州房价数据集<br />
housing = fetch_california_housing()<br />
X = pd.DataFrame(housing.data, columns=housing.feature_names)<br />
y = housing.target<br />
<br />
X_train, X_test, y_train, y_test = train_test_split(<br />
X, y, test_size=0.2, random_state=42<br />
)<br />
<br />
# 标准化<br />
scaler = StandardScaler()<br />
X_train_scaled = scaler.fit_transform(X_train)<br />
X_test_scaled = scaler.transform(X_test)</td>
</tr>
</tbody>
</table>

**题目列表**

|      |          |                                                                 |
|------|----------|-----------------------------------------------------------------|
| 题号 | 题目类型 | 需求描述                                                        |
| 1    | 模型训练 | 使用训练集训练线性回归模型，输出模型的截距和所有特征的系数      |
| 2    | 模型评估 | 在测试集上预测，计算MSE、RMSE、R²三个评估指标                   |
| 3    | 特征分析 | 根据系数排序，找出对房价影响最大的3个特征，并解释正负系数的含义 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：训练线性回归 ----------<br />
lr = LinearRegression()<br />
lr.fit(X_train_scaled, y_train)<br />
<br />
print("模型截距：", lr.intercept_)<br />
coef_df = pd.DataFrame({<br />
"特征": housing.feature_names,<br />
"系数": lr.coef_<br />
})<br />
print("\n特征系数：")<br />
print(coef_df)<br />
<br />
# ---------- 题2：模型评估 ----------<br />
y_pred = lr.predict(X_test_scaled)<br />
<br />
mse = mean_squared_error(y_test, y_pred)<br />
rmse = np.sqrt(mse)<br />
r2 = r2_score(y_test, y_pred)<br />
<br />
print(f"\n测试集MSE：{mse:.4f}")<br />
print(f"测试集RMSE：{rmse:.4f}")<br />
print(f"测试集R²：{r2:.4f}")<br />
<br />
# ---------- 题3：特征重要性排序 ----------<br />
coef_df["系数绝对值"] = coef_df["系数"].abs()<br />
coef_df = coef_df.sort_values("系数绝对值", ascending=False)<br />
print("\n特征影响排序（前3）：")<br />
print(coef_df.head(3))<br />
# 正系数：特征值越大，房价越高；负系数：特征值越大，房价越低</td>
</tr>
</tbody>
</table>

**四、逻辑回归与分类基础（第49天）**

**对应知识点：二分类建模、混淆矩阵、准确率/精确率/召回率/F1**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import load_iris<br />
from sklearn.linear_model import LogisticRegression<br />
from sklearn.metrics import confusion_matrix, accuracy_score,
precision_score, recall_score, f1_score<br />
from sklearn.model_selection import train_test_split<br />
from sklearn.preprocessing import StandardScaler<br />
<br />
# 构造二分类任务：山鸢尾 vs 非山鸢尾<br />
iris = load_iris()<br />
X = iris.data<br />
y = (iris.target == 0).astype(int) # 0:山鸢尾，1:其他<br />
<br />
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)<br />
scaler = StandardScaler()<br />
X_train_scaled = scaler.fit_transform(X_train)<br />
X_test_scaled = scaler.transform(X_test)</td>
</tr>
</tbody>
</table>

**题目列表**

|      |            |                                                                 |
|------|------------|-----------------------------------------------------------------|
| 题号 | 题目类型   | 需求描述                                                        |
| 1    | 二分类建模 | 训练逻辑回归模型，在测试集上预测类别，输出预测结果前10条        |
| 2    | 混淆矩阵   | 计算测试集的混淆矩阵，标注出真正例、假正例、真负例、假负例      |
| 3    | 分类指标   | 手动计算并调用sklearn函数分别计算：准确率、精确率、召回率、F1值 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：训练逻辑回归 ----------<br />
log_reg = LogisticRegression(random_state=42)<br />
log_reg.fit(X_train_scaled, y_train)<br />
y_pred = log_reg.predict(X_test_scaled)<br />
print("预测结果前10条：", y_pred[:10])<br />
<br />
# ---------- 题2：混淆矩阵 ----------<br />
cm = confusion_matrix(y_test, y_pred)<br />
print("\n混淆矩阵：")<br />
print(cm)<br />
# [[TN, FP],<br />
# [FN, TP]]<br />
tn, fp, fn, tp = cm.ravel()<br />
print(f"真负例TN：{tn}，假正例FP：{fp}")<br />
print(f"假负例FN：{fn}，真正例TP：{tp}")<br />
<br />
# ---------- 题3：分类指标 ----------<br />
# 手动计算<br />
acc_manual = (tp + tn) / (tp + tn + fp + fn)<br />
precision_manual = tp / (tp + fp)<br />
recall_manual = tp / (tp + fn)<br />
f1_manual = 2 * precision_manual * recall_manual / (precision_manual +
recall_manual)<br />
<br />
# sklearn计算<br />
acc = accuracy_score(y_test, y_pred)<br />
precision = precision_score(y_test, y_pred)<br />
recall = recall_score(y_test, y_pred)<br />
f1 = f1_score(y_test, y_pred)<br />
<br />
print(f"\n准确率：{acc:.4f}")<br />
print(f"精确率：{precision:.4f}")<br />
print(f"召回率：{recall:.4f}")<br />
print(f"F1值：{f1:.4f}")</td>
</tr>
</tbody>
</table>

**五、决策树与随机森林（第50-51天）**

**对应知识点：决策树可视化、特征重要性、随机森林、交叉验证**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import load_iris<br />
from sklearn.tree import DecisionTreeClassifier, plot_tree<br />
from sklearn.ensemble import RandomForestClassifier<br />
from sklearn.model_selection import cross_val_score<br />
import matplotlib.pyplot as plt<br />
<br />
iris = load_iris()<br />
X = iris.data<br />
y = iris.target</td>
</tr>
</tbody>
</table>

**题目列表**

|      |                    |                                                      |
|------|--------------------|------------------------------------------------------|
| 题号 | 题目类型           | 需求描述                                             |
| 1    | 决策树训练与可视化 | 训练深度为3的决策树分类器，绘制决策树可视化图        |
| 2    | 特征重要性         | 输出决策树模型的特征重要性排序，对应到4个鸢尾花特征  |
| 3    | 随机森林+交叉验证  | 训练含100棵树的随机森林，用5折交叉验证输出平均准确率 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：决策树可视化 ----------<br />
dt = DecisionTreeClassifier(max_depth=3, random_state=42)<br />
dt.fit(X, y)<br />
<br />
plt.figure(figsize=(12, 8))<br />
plot_tree(dt,<br />
feature_names=iris.feature_names,<br />
class_names=iris.target_names,<br />
filled=True, rounded=True, fontsize=10)<br />
plt.title("鸢尾花分类决策树")<br />
plt.tight_layout()<br />
plt.show()<br />
<br />
# ---------- 题2：特征重要性 ----------<br />
feature_importance = pd.DataFrame({<br />
"特征": iris.feature_names,<br />
"重要性": dt.feature_importances_<br />
}).sort_values("重要性", ascending=False)<br />
print("特征重要性排序：")<br />
print(feature_importance)<br />
<br />
# ---------- 题3：随机森林+交叉验证 ----------<br />
rf = RandomForestClassifier(n_estimators=100, random_state=42)<br />
cv_scores = cross_val_score(rf, X, y, cv=5, scoring="accuracy")<br />
<br />
print(f"\n5折交叉验证准确率：{cv_scores}")<br />
print(f"平均准确率：{cv_scores.mean():.4f}")<br />
print(f"准确率标准差：{cv_scores.std():.4f}")</td>
</tr>
</tbody>
</table>

**六、聚类算法（第52天）**

**对应知识点：K-Means、肘部法则选K、DBSCAN、聚类可视化**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import make_blobs<br />
from sklearn.cluster import KMeans, DBSCAN<br />
from sklearn.preprocessing import StandardScaler<br />
<br />
# 生成5个簇的模拟数据<br />
X, y_true = make_blobs(<br />
n_samples=500, centers=5, cluster_std=1.2, random_state=42<br />
)<br />
X_scaled = StandardScaler().fit_transform(X)</td>
</tr>
</tbody>
</table>

**题目列表**

|      |             |                                                             |
|------|-------------|-------------------------------------------------------------|
| 题号 | 题目类型    | 需求描述                                                    |
| 1    | K-Means聚类 | 设置n_clusters=5训练K-Means，绘制聚类结果散点图，标注簇中心 |
| 2    | 肘部法则选K | 测试k从2到10的所有情况，绘制肘部法则图，找出最佳簇数        |
| 3    | DBSCAN聚类  | 使用DBSCAN算法对同一数据聚类，对比和K-Means的结果差异       |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：K-Means聚类 ----------<br />
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)<br />
y_kmeans = kmeans.fit_predict(X_scaled)<br />
<br />
plt.figure(figsize=(8, 6))<br />
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_kmeans, cmap="viridis",
s=30, alpha=0.7)<br />
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,
1],<br />
s=200, c="red", marker="*", label="簇中心")<br />
plt.title("K-Means聚类结果（k=5）")<br />
plt.legend()<br />
plt.tight_layout()<br />
plt.show()<br />
<br />
# ---------- 题2：肘部法则 ----------<br />
inertias = []<br />
k_range = range(2, 11)<br />
for k in k_range:<br />
km = KMeans(n_clusters=k, random_state=42, n_init=10)<br />
km.fit(X_scaled)<br />
inertias.append(km.inertia_)<br />
<br />
plt.figure(figsize=(8, 4))<br />
plt.plot(k_range, inertias, "bo-")<br />
plt.xlabel("簇数k")<br />
plt.ylabel("簇内平方和inertia")<br />
plt.title("肘部法则选择最佳k值")<br />
plt.grid(alpha=0.3)<br />
plt.tight_layout()<br />
plt.show()<br />
# 拐点在k=5处，为最佳簇数<br />
<br />
# ---------- 题3：DBSCAN聚类 ----------<br />
dbscan = DBSCAN(eps=0.3, min_samples=5)<br />
y_dbscan = dbscan.fit_predict(X_scaled)<br />
<br />
plt.figure(figsize=(8, 6))<br />
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_dbscan, cmap="viridis",
s=30, alpha=0.7)<br />
plt.title("DBSCAN聚类结果（-1为异常点）")<br />
plt.tight_layout()<br />
plt.show()<br />
<br />
print(f"DBSCAN识别出的簇数：{len(set(y_dbscan)) - (1 if -1 in y_dbscan
else 0)}")<br />
print(f"异常点数量：{sum(y_dbscan == -1)}")</td>
</tr>
</tbody>
</table>

**七、模型评估指标（第53天）**

**对应知识点：ROC曲线、AUC值、多分类评估、回归评估综合**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.datasets import make_classification<br />
from sklearn.linear_model import LogisticRegression<br />
from sklearn.model_selection import train_test_split<br />
from sklearn.metrics import roc_curve, roc_auc_score,
classification_report, precision_score, recall_score<br />
<br />
# 生成二分类数据集<br />
X, y = make_classification(<br />
n_samples=1000, n_features=10, n_classes=2, random_state=42<br />
)<br />
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)<br />
<br />
model = LogisticRegression()<br />
model.fit(X_train, y_train)<br />
y_pred_proba = model.predict_proba(X_test)[:, 1] # 正类概率<br />
y_pred = model.predict(X_test)</td>
</tr>
</tbody>
</table>

**题目列表**

|      |              |                                                        |
|------|--------------|--------------------------------------------------------|
| 题号 | 题目类型     | 需求描述                                               |
| 1    | ROC曲线与AUC | 绘制ROC曲线，计算AUC值，解释AUC的业务含义              |
| 2    | 分类报告     | 输出完整分类报告，包含精确率、召回率、F1、支持数       |
| 3    | 阈值调整     | 将分类阈值从默认0.5调整为0.3，对比精确率和召回率的变化 |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：ROC曲线与AUC ----------<br />
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)<br />
auc = roc_auc_score(y_test, y_pred_proba)<br />
<br />
plt.figure(figsize=(7, 6))<br />
plt.plot(fpr, tpr, "b-", linewidth=2, label=f"AUC = {auc:.4f}")<br />
plt.plot([0, 1], [0, 1], "r--", label="随机猜测")<br />
plt.xlabel("假正率FPR")<br />
plt.ylabel("真正率TPR")<br />
plt.title("ROC曲线")<br />
plt.legend()<br />
plt.grid(alpha=0.3)<br />
plt.tight_layout()<br />
plt.show()<br />
#
AUC含义：随机抽取一个正样本和一个负样本，模型给正样本打分更高的概率<br />
<br />
# ---------- 题2：完整分类报告 ----------<br />
print("分类报告：")<br />
print(classification_report(y_test, y_pred))<br />
<br />
# ---------- 题3：阈值调整 ----------<br />
threshold = 0.3<br />
y_pred_new = (y_pred_proba &gt;= threshold).astype(int)<br />
<br />
precision_new = precision_score(y_test, y_pred_new)<br />
recall_new = recall_score(y_test, y_pred_new)<br />
<br />
print(f"\n默认阈值0.5 - 精确率：{precision_score(y_test,
y_pred):.4f}，召回率：{recall_score(y_test, y_pred):.4f}")<br />
print(f"调整阈值0.3 -
精确率：{precision_new:.4f}，召回率：{recall_new:.4f}")<br />
#
降低阈值：召回率上升，精确率下降（更多样本被判为正类，漏判减少，误判增加）</td>
</tr>
</tbody>
</table>

**八、超参数调优（第54天）**

**对应知识点：网格搜索、随机搜索、交叉验证调参**

**初始化代码**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
from sklearn.ensemble import RandomForestClassifier<br />
from sklearn.model_selection import GridSearchCV,
RandomizedSearchCV<br />
from sklearn.datasets import load_iris<br />
from sklearn.metrics import accuracy_score<br />
<br />
iris = load_iris()<br />
X = iris.data<br />
y = iris.target<br />
base_model = RandomForestClassifier(random_state=42)</td>
</tr>
</tbody>
</table>

**题目列表**

|      |                      |                                                                                            |
|------|----------------------|--------------------------------------------------------------------------------------------|
| 题号 | 题目类型             | 需求描述                                                                                   |
| 1    | 网格搜索GridSearch   | 对随机森林的n_estimators、max_depth两个参数做网格搜索，5折交叉验证，输出最优参数和最优得分 |
| 2    | 随机搜索RandomSearch | 增加更多参数维度，用随机搜索做20次迭代，对比网格搜索的效率和结果                           |
| 3    | 最优模型预测         | 用调参后的最优模型在全量数据上预测，输出最终准确率                                         |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Python<br />
# ---------- 题1：网格搜索 ----------<br />
param_grid = {<br />
"n_estimators": [50, 100, 200],<br />
"max_depth": [3, 5, 7, None]<br />
}<br />
<br />
grid_search = GridSearchCV(<br />
base_model, param_grid, cv=5, scoring="accuracy", n_jobs=-1<br />
)<br />
grid_search.fit(X, y)<br />
<br />
print("网格搜索最优参数：", grid_search.best_params_)<br />
print("网格搜索最优准确率：", grid_search.best_score_)<br />
<br />
# ---------- 题2：随机搜索 ----------<br />
param_dist = {<br />
"n_estimators": range(50, 300, 10),<br />
"max_depth": [3, 5, 7, 10, None],<br />
"min_samples_split": range(2, 10),<br />
"min_samples_leaf": range(1, 5),<br />
"bootstrap": [True, False]<br />
}<br />
<br />
random_search = RandomizedSearchCV(<br />
base_model, param_dist, n_iter=20, cv=5, scoring="accuracy",<br />
random_state=42, n_jobs=-1<br />
)<br />
random_search.fit(X, y)<br />
<br />
print("\n随机搜索最优参数：", random_search.best_params_)<br />
print("随机搜索最优准确率：", random_search.best_score_)<br />
#
随机搜索在参数维度多时效率更高，适合大范围粗筛；网格搜索适合小范围精调<br />
<br />
# ---------- 题3：最优模型预测 ----------<br />
best_model = random_search.best_estimator_<br />
y_pred = best_model.predict(X)<br />
final_acc = accuracy_score(y, y_pred)<br />
print(f"\n最优模型全量数据准确率：{final_acc:.4f}")</td>
</tr>
</tbody>
</table>
