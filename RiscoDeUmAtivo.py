import numpy as np
import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='N0D53X82CSFYKDIB', output_format='pandas')

PG, metadata = ts.get_daily_adjusted('PG',outputsize='full')
BEYER, metadata = ts.get_daily_adjusted('BEI.DE',outputsize='full')

sec_data = pd.DataFrame()

PG = PG.iloc[::-1]
BEYER = BEYER.iloc[::-1]


sec_data['PG'] = PG['5. adjusted close']
sec_data['BEYER'] = BEYER['5. adjusted close']

sec_data = sec_data.loc['2007-01-01'::]

print(sec_data)

sec_returns = np.log(sec_data / sec_data.shift(1))

##sec_returns['BEYER'] = (sec_returns['BEYER'].mean()*250)*100

PG_retorno_medio_diario = sec_returns['PG'].mean()*250
BEYER_retorno_medio_diario = sec_returns['BEYER'].mean()*250

Desvio_Padrão_PG = sec_returns['PG'].std()*250**0.5
Desvio_Padrão_BEYER = sec_returns['BEYER'].std()*250**0.5

###################

labels = ['PG', 'BEYER']
PGPlot = [PG_retorno_medio_diario, Desvio_Padrão_PG]
BEYERPlot = [BEYER_retorno_medio_diario, Desvio_Padrão_BEYER]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, PGPlot, width, label='Retorno Medio')
rects2 = ax.bar(x + width/2, BEYERPlot, width, label='Desvio Padrão')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Retorno Medio e Desvio Padrão')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()