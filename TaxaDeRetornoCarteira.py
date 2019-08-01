from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ts = TimeSeries(key='N0D53X82CSFYKDIB', output_format='pandas')

##Pegando as informações dos papeis
ITUB4, metadata = ts.get_daily_adjusted('ITUB4.SA',outputsize='full')
PETR4, metadata = ts.get_daily_adjusted('PETR4.SA',outputsize='full')
ABEV3, metadata = ts.get_daily_adjusted('ABEV3.SA',outputsize='full')
VALE3, metadata = ts.get_daily_adjusted('VALE3.SA',outputsize='full')

#invertendo a ordem para do mais antigo para o mais novo

ITUB4 = ITUB4.iloc[::-1]
PETR4 = PETR4.iloc[::-1]
ABEV3 = ABEV3.iloc[::-1]
VALE3 = VALE3.iloc[::-1]

mydata = pd.DataFrame()

##selecionando apenas o fechamento ajustado

mydata['ITUB4'] = ITUB4['5. adjusted close']
mydata['PETR4'] = PETR4['5. adjusted close']
mydata['ABEV3'] = ABEV3['5. adjusted close']
mydata['VALE3'] = VALE3['5. adjusted close']

#Usando o iloc para indexar a partir da primeira data

mydata.iloc[0]

#Plotando a taxa de retorno da carteira nos gráficos

(mydata/mydata.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

returns = (mydata/mydata.shift(1))-1

print(returns.head())

weights = np.array([0.25,0.25,0.25,0.25])

annual_returns = returns.mean()*250

print(annual_returns)

pfolio = round(np.dot(annual_returns,weights),2)*100

##Não trata valores faltantes