import numpy as np
import pandas as pd

from scipy import stats 
import matplotlib.pyplot as plt 
import statsmodels.api as sm


data = pd.read_excel('/home/leslye/Área de Trabalho/Python /Housing.xlsx')
 


X = data['House Size (sq.ft.)']
Y = data['House Price']

plt.scatter(X,Y)
plt.axis([0,2500,0,1500000])
plt.ylabel('House Price')
plt.xlabel('House Size')

X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()

print(reg.summary())

teste = 260800+402*1000
print(teste)