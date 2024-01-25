from sklearn import datasets
import pandas as pd

# 加载加州房价数据集
california_housing = datasets.fetch_california_housing()

# 创建DataFrame对象
df = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
df['MedHouseVal'] = california_housing.target  # 将房价添加到DataFrame中

# 将数据集保存到Excel文件中
df.to_excel('california_housing.xlsx', sheet_name='california_housing', index=False)

# 打印数据集表格属性
print(df)
