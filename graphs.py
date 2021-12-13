import pandas as pd
import matplotlib.pyplot as plt

def creating_graph(datastock, stock):
    datastock.index = pd.DatetimeIndex(datastock.index)
    datastock.rename(columns=lambda s: s[3:], inplace=True)
    while True:
        try:
            timeframe= int(input("How many business days would you like to see? (1-40)"))
            break
        except ValueError:
            print("Oops! Not a number. Try again... ")
    if 0 < timeframe < 41:
        datatoplot = datastock.close.resample('B').last().iloc[40 - timeframe:1000]
    else:
        return print("This is an invalid number of days. You will be sent to the main menu.")


    #Draw the graph
    fig = datatoplot.plot()
    fig.set_ylabel('USD')
    fig.set_title(f'Stock price of {stock}')
    #fig.set_xlim(dt.datetime(2021, 12, 8, 14, 30), dt.datetime(2021,12,8, 16))

    #Show the graph
    plt.show()