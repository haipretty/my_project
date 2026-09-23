
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(2026)

##第46天，对应知识点：机器学习分类、Sklearn安装、数据集加载、训练集划分
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#题目1：
#分类模型预测类别、回归模型预测连续值，都是带标签训练的，属于监督学习
#聚类相似数据分组、降维，都是不带标签训练的，属于非监督学习

#题目2：
data = load_iris()
feature_names = data.feature_names
label_names = data.target_names
dimention = data.data.shape

# print("feature_names: ", feature_names)
# print("label_names: ", label_names)
# print("dimention: ", dimention)

#题目3：
X = pd.DataFrame(data.data, columns=feature_names)
# print(X.head())

y = data.target
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# print("训练集样本数量：", X_train.shape[0])
# print("测试集样本数量：", X_test.shape[0])


##第47天，对应知识点：缺失值处理、标准化、归一化、分类编码、Pipeline流水线
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

#生成带缺失值、分类特征的模拟数据
#1.加载数据
df = pd.DataFrame({
    "年龄": [25, 30, np.nan, 45, 35, 28, 50, np.nan, 32, 40],
    "收入": [5000, 8000, 6500, 12000, 9000, np.nan, 15000, 7000, 8500, 11000],
    "性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男", "女"],
    "城市": ["北京", "上海", "广州", "深圳", "北京", "上海", "广州", "深圳", "北京", "上海"],
    "是否流失": [0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
})

#2.提取特征
X = df.drop("是否流失", axis=1)
y = df["是否流失"]

#题目1：缺失值处理
number_columns = ["年龄", "收入"]
imputer = SimpleImputer(strategy="mean")                        #SimpleImputer只能用于数值列
X_imputed = imputer.fit_transform(X[number_columns])
# print(X_imputed)

#题目2：分类编码
label = LabelEncoder()
X_label_encoded = label.fit_transform(X["性别"])                #转换成整数
# print(X_label_encoded)

encoder = OneHotEncoder(sparse_output=False, drop="first")      #转换成每个类别一个列
city_encoded = encoder.fit_transform(X[["城市"]])
city_df = pd.DataFrame(city_encoded, columns=encoder.get_feature_names_out())   #转成df
X_encoded = pd.concat([X, city_df], axis=1)
# print(X_encoded)

#题目3：数值缩放
std_scaler = StandardScaler()
X_std_scaled = std_scaler.fit_transform(X[number_columns])
# print(X_std_scaled)

MM_scaler = MinMaxScaler()
X_MM_scaled = MM_scaler.fit_transform(X[number_columns])
# print(X_MM_scaled)

#题目4：Pipeline流水线
# preprocessor = ColumnTransformer([
#     ("imputer", SimpleImputer(strategy="mean"), number_columns),      #错误用法
#     ("scaler", StandardScaler(), number_columns),
#     ("encoder", OneHotEncoder(), ["性别", "城市"])
# ])

num_pipeline = Pipeline([                                   #pipeline每个步骤按序执行
    ("impute", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])
preprocessor = ColumnTransformer([                          #列转换器每一项独立并行执行
    ("num", num_pipeline, number_columns),
    ("category", OneHotEncoder(sparse_output=False, drop="first"), ["性别", "城市"])
])

X_preprocessed = preprocessor.fit_transform(X)
# print(X_preprocessed)


##第48天，对应知识点：线性回归建模、MSE/RMSE/R²评估、特征系数解释
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#加载数据集
housing = fetch_california_housing()

#特征提取
X = housing.data                #特征矩阵
y = housing.target              #目标向量
# print(X.shape)

#划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)                    #不能再训练

#题目1：模型训练
model = LinearRegression()
model.fit(X_train_scaled, y_train)

coef_df = pd.DataFrame({
    "特征": housing.feature_names,
    "系数": model.coef_                                     #回归系数
})
# # print(f"模型的截距：{model.intercept_}")
# print(f"模型的系数：\n{coef_df}") 

#题目2：模型评估
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)                                         #均方根误差
r2 = r2_score(y_test, y_pred)
# print(f"均方误差：{mse}")
# print(f"均方根误差：{rmse:.4f}")
# print(f"决定系数：{r2}")                                   #决定系数？？

#题目3：特征分析                                        
#根据系数排序，找出对房价影响最大的3个特征，并解释正负系数的含义
coef_df["系数abs"] = coef_df["系数"].abs()
coef_df.sort_values("系数abs", ascending=False, inplace=True)
# print(f"对房价影响最大的3个特征：\n{coef_df.head(3)}")


##第49天，对应知识点：二分类建模、混淆矩阵、准确率/精确率/召回率/F1
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#加载数据集
iris = load_iris()

#提取特征和标签
X = iris.data
y = (iris.target == 0).astype(int)

#划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#标准化
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)        #测试集只有transfrom

#题目1：二分类建模
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
# print(y_pred[:10])

#题目2：混淆矩阵
cm = confusion_matrix(y_test, y_pred)
# print(cm)                                     #标注出真负例、假正例、假负例、真正例
tn, fp, fn, tp = cm.ravel()                     #= flatten() = reshape(-1)
# print(f"真负例TN：{tn}，假正例FP：{fp}")
# print(f"假负例FN：{fn}，真正例TP：{tp}")         

#题目3：分类指标
acc_manual = (tn+tp) / (tn+fn+fp+tp)            #通过混淆矩阵计算分类指标
prec_manual = tp / (tp+fp)
reca_manual = tp / (tp+fn)
f1_manual = (2*prec_manual*reca_manual) / (prec_manual+reca_manual)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall =recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# print(f"准确率：{accuracy, acc_manual}")
# print(f"精确率：{precision, prec_manual}")
# print(f"召回率：{recall, reca_manual}")
# print(f"f1分数：{f1, f1_manual}")


#第50-51天，对应知识点：决策树可视化、特征重要性、随机森林、交叉验证
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#题目1：决策树训练和可视化
model_dt = DecisionTreeClassifier(max_depth=3)          #深度为3，分裂3次
model_dt.fit(X, y)

# plot_tree(model_dt)
plt.figure(figsize=(12, 8))
plot_tree(model_dt,                                     #决策树画图
          feature_names=iris.feature_names,             #基尼不纯度
          class_names=iris.target_names,
          filled=True, rounded=True, fontsize=10)
plt.title("鸢尾花分类决策树")
plt.tight_layout()
# plt.show()

#题目2：特征重要性
feature_importance = pd.DataFrame({
    "特征": iris.feature_names,
    "重要性": model_dt.feature_importances_             #决策树特征重要性
})

tree = model_dt.tree_
# print(f"树结构：{tree}")
# print(f"分裂特征的索引：{tree.feature}")
# print(f"分裂特征：{[iris.feature_names[x] for x in tree.feature]}")
# print(f"分裂阈值：{tree.threshold}")
# print(f"左子节点：{tree.children_left}")
# print(f"右子节点：{tree.children_right}")
# print(f"节点gini：{tree.impurity}")
# print(f"节点样本数：{tree.n_node_samples}")
# print(f"节点类别分布：{tree.value}")

# print(feature_importance.sort_values("重要性", ascending=False))

#题目3：随机森林+交叉验证
model_rand = RandomForestClassifier(n_estimators=100)                       #模型不用提前训练
cross_scores = cross_val_score(model_rand, X, y, cv=5, scoring="accuracy")  #准确率得分
# print(f"交叉验证平均准确率：{cross_scores.mean()}")                           #平均得分
# print(f"交叉验证准确率标准差：{cross_scores.std()}")                          #得分标准差


##第52天，对应知识点：K-Means、肘部法则选K、DBSCAN、聚类可视化
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

#生成5个簇的模拟数据
X, y_true = make_blobs(n_samples=500, centers=5, cluster_std=1.2, random_state=42)
X_scaled = StandardScaler().fit_transform(X)

#题目1：K-Means聚类
kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)     #n_init？？
y_kmeans = kmeans.fit_predict(X_scaled)                    #绘制聚类结果散点图，标注簇中心？？

# print("训练数据：", X_scaled.shape, X_scaled[:5])
# print("===================")
# print("预测结果（每个样本点属于的簇索引）：", y_kmeans.shape, y_kmeans[:5])
# print("簇索引列表", np.unique(y_kmeans))
# print("===================")
# print("簇中心坐标：", kmeans.cluster_centers_)

plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_kmeans, cmap="viridis", s=30, alpha=0.7)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c="red", s=200, marker="*", label="簇中心")
plt.title("K-Means聚类结果（k=5）")
plt.legend()
plt.tight_layout()
# plt.show()

#题目2：肘部法则选K
#测试k从2到10的所有情况，绘制肘部法则图，找出最佳簇数？？
inertias = []
k_range = range(2, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(k_range, inertias, "bo-")
plt.xlabel("簇数k")
plt.ylabel("簇内平方和inertia")
plt.title("肘部法则选择最佳k值")
plt.grid(alpha=0.3)
plt.tight_layout()
# plt.show()

#题目3：密度聚类DBSCAN
#使用DBSCAN算法对同一数据聚类，对比和K-Means的结果差异
model_db = DBSCAN(eps=0.3, min_samples=5)
y_db = model_db.fit_predict(X_scaled)

plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_db, cmap="viridis", s=30, alpha=0.7)
plt.title("DBSCAN聚类结果（-1为异常点）")
plt.colorbar()
plt.tight_layout()
# plt.show()

# print(f"DBSCAN识别出的簇数：{len(set(y_db)) - (1 if -1 in y_db else 0)}")
# print(f"异常点数量：{sum(y_db == -1)}")


##第53天，对应知识点：ROC曲线、AUC值、多分类评估、回归评估综合
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, precision_score, recall_score

#加载数据集
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
# print(X[:10])
# print(y[:10])

#划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#初始化逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred_probability = model.predict_proba(X_test)        #样本属于每个类别的概率矩阵
y_pred_proba = y_pred_probability[:, 1]                 #预测为正类（1）的概率
y_pred = model.predict(X_test)

#题目1：ROC曲线与AUC，评估二分类模型的性能
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)   #ROC曲线
#y_test：真实标签0或1
#y_pred_proba：模型预测为正类的概率
#fpr：假正率=FP/(FP+TN)=误报率（越低越好）
#tpr：真正率=TP/(TP+FN)=召回率（越高越好）

auc = roc_auc_score(y_test, y_pred_proba)               #AUC指标
#AUC = 1	完美分类器，所有正例排在负例前面（y_pred_proba中正例概率大，负例概率小）
#AUC = 0.5	和随机猜一样（对角线）
#AUC < 0.5	比随机还差

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, "b-", linewidth=2, label=f"AUC = {auc:.4f}")
plt.plot([0,1], [0,1], "r--", label="随机猜测(AUC = 0.5)")
plt.xlabel("假正率FPR")
plt.ylabel("真正率TPR")
plt.title("ROC曲线")
plt.legend(loc="upper left")
plt.grid(alpha=0.3)
plt.tight_layout()
# plt.show()

#题2：分类报告
#输出完整分类报告，包含精确率、召回率、F1、支持数
report =classification_report(y_test, y_pred)
# print(report)

#题3：
#将分类阈值从默认0.5调整为0.3，对比精确率和召回率的变化
threshold = 0.3
y_pred_new = (y_pred_proba >= threshold).astype(int)
precision_new = precision_score(y_test, y_pred_new)
recall_new = recall_score(y_test, y_pred_new)

# print(f"默认阈值0.5 - 精确率：{precision_score(y_test, y_pred):.4f}，\
#       召回率：{recall_score(y_test, y_pred):.4f}")
# print(f"阈值0.3 - 精确率：{precision_new:.4f}，召回率：{recall_new:.4f}")


#第54天，对应知识点：网格搜索、随机搜索、交叉验证调参
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

#加载数据集
iris = load_iris()

#提取特征和标签
X = iris.data
y = iris.target
base_model = RandomForestClassifier(random_state=42)

#题目1：网格搜索
#对随机森林的n_estimators、max_depth两个参数做网格搜索，5折交叉验证，输出最优参数和最优得分
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 7, None]
}
grid_search = GridSearchCV(base_model, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search.fit(X, y)
base_model_grid = grid_search.best_estimator_

# print(grid_search.best_params_)
# print(grid_search.best_score_)

#题目2：随机搜索
#增加更多参数维度，用随机搜索做20次迭代，对比网格搜索的效率和结果
param_dist = {
    "n_estimators": range(50, 300, 10),
    "max_depth": [3, 5, 7, 10, None],
    "min_samples_split": range(2, 10),
    "min_samples_leaf": range(1, 5),
    "bootstrap": [True, False]
}
random_search = RandomizedSearchCV(base_model, param_dist, n_iter=20, cv=5, scoring="accuracy", random_state=42, n_jobs=-1)
random_search.fit(X, y)
base_model_random = random_search.best_estimator_

# print(random_search.best_params_)
# print(random_search.best_score_)

#题目3：最优模型预测
#用调参后的最优模型在全量数据上预测，输出最终准确率

y_pred_grid = base_model_grid.predict(X)
y_pred_random = base_model_random.predict(X)

print(f"网格搜索最佳模型的准确率：{accuracy_score(y, y_pred_grid):.4f}")
print(f"随机搜索最佳模型的准确率：{accuracy_score(y, y_pred_random):.4f}")

