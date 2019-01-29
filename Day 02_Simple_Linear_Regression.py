#数据预处理

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('datasets/studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 

print("---------------------")
print('X_train')
print(X_train)

print('Y_train')
print(Y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

print('X_test')
print(X_test)

print('Y_pred')
print(Y_pred)

plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
#plt.show()

plt.scatter(X_test , Y_test, color = 'pink')
plt.plot(X_test , regressor.predict(X_test), color ='green')
plt.show()

