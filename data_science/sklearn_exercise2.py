
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline  import Pipeline
from sklearn.compose import ColumnTransformer

###项目2：预测房价
##1.生成数据
#模拟数据：房屋面积 (平方米)、房间数、楼层、建造年份、位置（类别变量）
data = {
    'area': [70, 85, 100, 120, 60, 150, 200, 80, 95, 110],
    'rooms': [2, 3, 3, 4, 2, 5, 6, 3, 3, 4],
    'floor': [5, 2, 8, 10, 3, 15, 18, 7, 9, 11],
    'year_built': [2005, 2010, 2012, 2015, 2000, 2018, 2020, 2008, 2011, 2016],
    'location': ['Chaoyang', 'Haidian', 'Chaoyang', 'Dongcheng', 'Fengtai', 'Haidian', 'Chaoyang', 'Fengtai', 'Dongcheng', 'Haidian'],
    'price': [5000000, 6000000, 6500000, 7000000, 4500000, 10000000, 12000000, 5500000, 6200000, 7500000]  # 房价（目标变量）
}
df = pd.DataFrame(data)

#查看数据
# print(df.head())

##2.数据预处理
#提取特征和标签
X = df.drop(columns="price")
y = df["price"]
# print(X, y)

#划分数据集
X_tran, X_test, y_tran, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#构建预处理步骤
numeric_features = ["area", "rooms", "floor", "year_built"]
categorical_features = ["location"]

numeric_transformer = Pipeline(steps=[      #Pipeline可以当转化器或估计器来用
    ("scaler", StandardScaler())            #数值特征标准化
])

categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))  #忽略新类别
])

#将两个转换器组合成ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cate", categorical_transformer, categorical_features)
    ]
)

#查看预处理后的数据
X_train_transformed = preprocessor.fit_transform(X_tran)
# print(f"预处理后的训练数据：\n{X_train_transformed}")

##3.建立模型
#构建包含预处理和回归模型的Pipeline
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),     #组合后的转换器
    ("regressor", LinearRegression())   #回归模型
])

#训练模型
model_pipeline.fit(X_tran, y_tran)

#预测
y_pred = model_pipeline.predict(X_test)
print(X_test)
print(f"预测结果：\n{y_pred}")


##4.模型评估（回归模型）
#计算均方误差MSE 和 决定系数R2
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"均方误差（MSE）：{mse:.2f}")
print(f"决定系数（R2）：{r2:.2f}")


##5.模型优化（线性回归没有太多超参数可调）
#线性回归的参数网格（仅调整拟合截距fit_intercept）
param_grid = {
    "regressor__fit_intercept": [True, False]    #是否拟合截距
}

grid_search = GridSearchCV(model_pipeline, param_grid, cv=5, scoring="neg_mean_squared_error", verbose=1)
grid_search.fit(X_tran, y_tran)
# print(f"最佳参数：\n{grid_search.best_params_}")

#使用最佳模型进行预测
best_model = grid_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)
# print(best_model)

#再次评估模型
mse_opt = mean_squared_error(y_test, y_pred_optimized)
r2_opt = r2_score(y_test, y_pred_optimized)
# print(f"优化后的均方误差（MSE）：{mse_opt:.2f}")
# print(f"优化后的决定系数（R2）：{r2_opt:.2f}")

