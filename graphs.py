import pandas as pd
import matplotlib.pyplot as plt

def creating_graph(datastock, stock):
    datastock.index = pd.DatetimeIndex(datastock.index)
    datastock.rename(columns=lambda s: s[3:], inplace=True)
    datatoplot = datastock.close.resample('B').last().iloc[0:30]

    #Draw the graph
    fig = datatoplot.plot()
    fig.set_ylabel('Eur')
    fig.set_title(f'Stock price of {stock}')
    #fig.set_xlim(dt.datetime(2021, 12, 8, 14, 30), dt.datetime(2021,12,8, 16))

    #Show the graph
    plt.show()