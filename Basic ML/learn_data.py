import pandas
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pandas.read_csv('customers-100000.csv')
data = pandas.read_csv('products-1000.csv')
# print(dataset.head(10))
# print(dataset.info())
# print(data.shape)
# print(data.head(10))
# print(data.isnull().sum())
print(data.isnull().sum().sum())
print(data.notnull().sum().sum())
# print(data.isnull().sum()/data.shape[0]*100)
sns.heatmap(data.notnull())
print(plt.show())