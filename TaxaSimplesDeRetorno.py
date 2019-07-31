##coding: utf-8

from alpha_vantage.timeseries import TimeSeries
import numpy 
import matplotlib.pyplot as plt
import pandas

ts = TimeSeries(key='N0D53X82CSFYKDIB', output_format='pandas')
##PG é o nome da ação
PG, metadata = ts.get_daily_adjusted('PG')


print(PG.iloc[::-1])

PG = PG.iloc[::-1]

PG['simple_return']=(PG['5. adjusted close']/PG['5. adjusted close'].shift(1))-1
print(PG['simple_return'])
PG['simple_return'].plot(figsize=(8, 5))
plt.show() 

avg_returns_d = PG['simple_return'].mean()
avg_returns_a = PG['simple_return'].mean()*250

avg_returns_a*=100

print(round(avg_returns_a,2),"%")
