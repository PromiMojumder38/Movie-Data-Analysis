import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = 'https://www.kaggle.com/datasets/shivamb/netflix-shows'

data = pd.read_csv('IMDB-Movie-Data.csv')
#print(data.head())
#print(data.head(10))
#print(data.tail(10))
#print(data.shape[0])
#print(data.info())
#print(data.isnull().values.any())
#print(data.isnull())
#print(data.isnull().sum())

"""Checking null values 
print(sns.heatmap(data.isnull()))
plt.show()"""

"""dropping null values
data = data.dropna(axis=0)
print(sns.heatmap(data.isnull()))
plt.show()"""

"""checking duplicated data
print(data.duplicated().any())"""





