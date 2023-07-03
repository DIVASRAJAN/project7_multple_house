# -*- coding: utf-8 -*-
"""multiple_housing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I5DfysGzll_KxQ_HiFBk7SqBl35t5a_d
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/content/Housing.csv')
df.head()

df.tail()

df.describe()

df.info()

df.isna().sum()

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()

lst=['mainroad', 	'guestroom', 	'basement', 	'hotwaterheating', 	'airconditioning', 'prefarea' ,	'furnishingstatus']

for i in lst:
  df[i]=lb.fit_transform(df[i])

df.head()

x=df.iloc[:,1:].values
y=df.iloc[:,0].values

lt=['area', 	'bedrooms', 	'bathrooms', 	'stories', 	'mainroad', 	'guestroom', 	'basement', 	'hotwaterheating', 	'airconditioning', 	'parking', 	'prefarea',
    'furnishingstatus']


for i in lt:
  print(sns.regplot(x=df[i],y=y))
  plt.show()

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.30,random_state=42)

from sklearn.linear_model import LinearRegression
linear=LinearRegression()
linear.fit(xtr,ytr)
ypr=linear.predict(xts)

df1=pd.DataFrame({'actual':yts,'predicted':ypr,'differance':yts-ypr})
df1

print('slope is ')
print(list(zip(df.iloc[:,1:],linear.coef_)))
print('constant is ',linear.intercept_)

from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error,mean_squared_error

# absolute error
print('mae',mean_absolute_error(yts,ypr))
# maep
print('maep',mean_absolute_percentage_error(yts,ypr))
#mse
print('mse',mean_squared_error(yts,ypr))
#rmse
print('rmse',np.sqrt(mean_squared_error(yts,ypr)))

#r2 score

from sklearn.metrics import r2_score
print('r2 ',r2_score(yts,ypr))