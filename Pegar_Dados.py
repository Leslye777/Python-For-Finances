from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import quandl


ts = TimeSeries(key='N0D53X82CSFYKDIB', output_format='pandas')
##data, meta_data = ts.get_intraday(symbol='ABEV3.SA',interval='60min', outputsize='full')
##data['4. close'].plot(kind='')
##print(data)

data, metadata = ts.get_daily_adjusted('ABEV3.SA', outputsize='full')
l30 = data.head(31).copy()
print(l30['5. adjusted close'])
mydata01 = quandl.get("FRED/GDP")
print(mydata01)



##data.to_csv("PETR4")

##plt.title('Intraday Times Series for the PETR4(5 min)')
##plt.show()


