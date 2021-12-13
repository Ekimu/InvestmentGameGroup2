import pandas as pd
import matplotlib.pyplot as plt

def creating_graph(datastock, stock):
    datastock.index = pd.DatetimeIndex(datastock.index)
    datastock.rename(columns=lambda s: s[3:], inplace=True)
    timeframe = int(input("How many business days would you like to see? (1-40)"))
    if timeframe in [0,40]:
        datatoplot = datastock.close.resample('B').last().iloc[40 - timeframe:1000]
    else:
        return print("Invalid number of days.")


    #Draw the graph
    fig = datatoplot.plot()
    fig.set_ylabel('USD')
    fig.set_title(f'Stock price of {stock}')
    #fig.set_xlim(dt.datetime(2021, 12, 8, 14, 30), dt.datetime(2021,12,8, 16))

    #Show the graph
    plt.show()