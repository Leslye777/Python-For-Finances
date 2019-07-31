from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import numpy as np
import pandas

ts = TimeSeries(key='N0D53X82CSFYKDIB', output_format='pandas')
PG, metadata = ts.get_daily_adjusted('PG')

PG = PG.iloc[::-1]

PG['log_return']=np.log(PG['5. adjusted close']/PG['5. adjusted close'].shift(1))
print (PG['log_return'])

PG['log_return'].plot(figsize=(8,5))
plt.show()

log_returnd = PG['log_return'].mean()
log_returnc = PG['log_return'].mean()*250

log_returnc*100

log_returnc = round(log_returnc,2)

print(log_returnc,"%")

