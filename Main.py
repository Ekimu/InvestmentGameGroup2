from StockData import requesting_one_stock
from graphs import creating_graph

# Log in

# Show cash balance
print("Welcome to our Investment Game!!")
cash_balance = 10000
print(f"Your starting balance is {cash_balance} USD")

# 3.a Show portfolio
#1st draft of portfolio structure
Portfolio = {

}
# Portfolio = [
#     { 'name': 'IMB', 'stockamount': 100 },
#     { 'name': 'AMZN', 'stockamount': 40 },
#     { 'name': 'cash_balance', 'price': 3, 'stock': 30 },
#     { 'name': 'milk', 'price': 1, 'stock': 80 }
# ]

# 3.b Show changes in portfolio through a time period (day, week, month, year) with %

# 4.a Search stock (based on stock symbol, names, market, currency, etc.)
print("Here is a list of some common stocks:")
print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
print("You can choose any stock you want.")
print(f"Your current portfolio contains")
print(Portfolio)


while True:
    inspect=input("Would you like to inspect a stock: (y/n)")
    if inspect != "y":
        print("You decided not inspect any stock, we'll end here")
        break
    elif inspect == "y":
    while True:
        stock = input("Please select a stock: ")
        datastock = requesting_one_stock(stock)
        if datastock == 0:

        elif requesting_one_stock(stock) = df


        creating_graph(datastock, stock)

        currentprice = datastock["close"][0]
        buysell = input(f"Do you want to buy or sell {stock} stock for the current price {currentprice}? (b/s/n)")

    # 4.b Show changes in stock through a time period (day, week, month, year) with %


    #else #portfolio



    # Buy stocks
        if buysell == "b":
            amount = int(input("How many stocks do you want to buy?"))
            costs = amount * currentprice
            cash_balance = cash_balance - costs
            if stock in Portfolio:
                Portfolio[stock] += amount
            else:
                Portfolio[stock] = amount
            print("Your current portfolio consists of the following stock: ")
            print(Portfolio)
            print(costs)
            print(cash_balance)
    # Sell stocks
        if buysell == "s":
            amount = int(input("How many stocks do you want to buy?"))
            costs = amount * currentprice
            cash_balance = cash_balance + costs
            if stock in Portfolio:
                Portfolio[stock] -= amount
            else:
                Portfolio[stock] = -amount
            print("Your current portfolio consists of the following stock: ")
            print(Portfolio)
            print(costs)
            print(cash_balance)



# Compare (e.g. cash balance or portfolio) to other users
# Exit






