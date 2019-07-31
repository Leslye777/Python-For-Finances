import datetime as dt 
import matplotlib as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(1995,1,1)
end = dt.datetime.now()

df = web.DataReader('PG','yahoo',start,end)
##l30 = df.tail(31).copy()
print(df)
##l30.to_csv('ABEV3.SA')

