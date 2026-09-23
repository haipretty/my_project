
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

###项目1：预测鸢尾花种类
##1.数据加载
#加载鸢尾花数据集
data = load_iris()

#数据转换成DataFrame，方便查看
df = pd.DataFrame(data.data, columns=data.feature_names)    #data二维数组
df["target"] = data.target                                  #target一维数组
df["species"] = df["target"].apply(lambda x: data.target_names[x])
# print(df.head())


##2.数据可视化
#多变量配对图：特征的分布和它们之间的关系
# sns.pairplot(df.iloc[:, [0,1,2,3,5]], hue="species")
# plt.title("iris pairplot")
# plt.show()

#热力图：特征之间的相关性
# correlation_matrix = df.drop(columns=["target", "species"]).corr()
# sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True, fmt=".2f")
# plt.title("correlation heatmap")
# plt.tight_layout()
# plt.show()


##3.数据预处理
#提取特征和标签
X = df.drop(columns=["target", "species"])
y = df["target"]

#标准化特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)      #每列特征的均值为0，标准差为1
# print(X_scaled[:3])


##4.特征选择
selector = SelectKBest(f_classif, k=2)  #使用卡方检验选择2个最相关的特征
X_new = selector.fit_transform(X_scaled, y)

#打印选择的特征
selected_features = selector.get_support(indices=True)      #返回选择特征的索引位列表
# print(selected_features)
# print("Selected features: ", X.columns[selected_features])  #到原DataFrame找对应列名


##5.建立分类模型
##使用决策树分类器进行分类
#划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=42)

#初始化模型
model_dt = DecisionTreeClassifier(random_state=42)

#训练模型
model_dt.fit(X_train, y_train)

#预测
y_pred_dt = model_dt.predict(X_test)
# print(y_pred_dt)

#评估模型
accuracy_dt = accuracy_score(y_test, y_pred_dt)
# print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")

##使用支持向量机SVM进行分类
#初始化模型
model_svm = SVC(kernel="linear", random_state=42)

#训练模型
model_svm.fit(X_train, y_train)

#预测
y_pred_svm = model_svm.predict(X_test)

#模型评估
accuracy_svm = accuracy_score(y_test, y_pred_svm)
# print(f"SVM Accuracy: {accuracy_svm:.4f}")


##6.模型评估
#混淆矩阵
cm = confusion_matrix(y_test, y_pred_dt)
# print("Confusion Matrix (Decision Tree): ")
# print(cm)

#精度、召回率、F1分数
report = classification_report(y_test, y_pred_dt)
# print("Classification Report (Decision Tree): ")
# print(report)


##7.模型调优
##网格搜索调优：寻找最优的参数组合
#定义决策树的参数网格
param_grid = {
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

#初始化调优器
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42), 
                           param_grid=param_grid, cv=5)

#训练调优器
grid_search.fit(X_train, y_train)

#获取最佳参数和最佳模型
# print("Best Parameters: ", grid_search.best_params_)
best_model = grid_search.best_estimator_
# print(best_model)

#预测和评估
y_pred_dt_optimized = best_model.predict(X_test)
accuracy_dt_optimized = accuracy_score(y_test, y_pred_dt_optimized)
# print(f"Optimized Decision Tree Accuracy: {accuracy_dt_optimized:.4f}")

##交叉验证：评估模型在不同数据子集上的表现，避免过拟合(看得分是否波动大)
#进行5折交叉验证
cross_val_scores = cross_val_score(best_model, X_new, y, cv=5)  #用划分数据集前的数据
# print(f"Cross-validation Scores: {cross_val_scores}")
# print(f"Mean CV Accuracy: {cross_val_scores.mean():.4f}")
