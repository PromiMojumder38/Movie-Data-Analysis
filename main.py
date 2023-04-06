import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = 'https://www.kaggle.com/datasets/shivamb/netflix-shows'

data = pd.read_csv('IMDB-Movie-Data.csv')
#print(data.head())
#print(data.head(10))
#print(data.tail(10))
#print(data.shape[0])
print(data.info())



