import pandas as pd
import matplotlib.pyplot as plt

def creating_graph(datastock, stock):

    #####added
    datastock.index = pd.DatetimeIndex(datastock.index)
    datastock.rename(columns=lambda s: s[3:], inplace=True)
    #####end

    ########################################
    #Used the code from StockData
    #################

    #Draw a graph
    #datastock[['close']].plot()
    fig = datastock.close.resample('B').last()
    fig.plot()
    #fig.set_ylabel('Eur')
    #fig.set_title(f'Stock price of {stock}')
    #fig.set_xlim(dt.datetime(2021, 12, 8, 14, 30), dt.datetime(2021,12,8, 16))

    #show the graph
    plt.show()