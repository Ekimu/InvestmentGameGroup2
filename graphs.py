import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

#####added
df.index = pd.DatetimeIndex(df.index)
df.rename(columns=lambda s: s[3:], inplace=True)
#####end

########################################
#Used the code from StockData
#################

#Draw a graph
fig = df[['open', 'high', 'low', 'close']].plot()
fig.set_ylabel('Eur')
fig.set_title('Stock price')
fig.set_xlim(dt.datetime(2021, 12, 8, 14, 30), dt.datetime(2021,12,8, 16))


#show the graph
plt.show()