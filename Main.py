from StockData import requesting_one_stock
from graphs import creating_graph

# Startup message / Log in
username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")
print(f"Welcome to our Investment Game {username_input}!")

# 1. Show cash balance
cash_balance = 10000
print(f"Your starting balance is {cash_balance} USD")

# 2.a Show portfolio
Portfolio = {
}
print(f"Your current portfolio contains following stocks {Portfolio}")
# 1st draft of portfolio structure
# Portfolio = [
#     { 'name': 'IMB', 'stockamount': 100 },
#     { 'name': 'AMZN', 'stockamount': 40 },
#     { 'name': 'cash_balance', 'price': 3, 'stock': 30 },
#     { 'name': 'milk', 'price': 1, 'stock': 80 }
# ]



# 2.b Show changes in portfolio through a time period (day, week, month, year) with %



# 3.a Search stock (based on stock symbol, names, market, currency, etc.)
# 3.b Show changes in stock through a time period (day, week, month, year) with %
while True:
    inspect=input("Would you like to inspect a stock: (y/n)")
    if inspect != "y":
        print("You decided not inspect any stock, we'll end here")
        break
    elif inspect == "y":
        print("Here is a list of some common stocks:")
        print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
        while True:
            stock = input("Please select a stock (symbol): ")
            datastock = requesting_one_stock(stock)
            if datastock is None:
                continue

            creating_graph(datastock, stock)
            currentprice = datastock["close"][0]
            buysell = input(f"Do you want to buy or sell {stock} for the current price {currentprice}? (b/s/n)")


        # 4. Buy stocks
            if buysell == "b":
                amount = int(input(f"How many shares do you want to buy of {stock}?"))
                costs = amount * currentprice
                print(f"The total cost of the shares is: {costs}")
                cash_balance = cash_balance - costs
                if stock in Portfolio:
                    Portfolio[stock] += amount
                else:
                    Portfolio[stock] = amount
                print(f"Your current portfolio consists of the following stock: {Portfolio}")
                print(f"Your current balance is now: {cash_balance}")


        # 5. Sell stocks
            if buysell == "s":
                amount = int(input(f"How many shares do you want to sell of {stock}?"))
                sellprice = amount * currentprice
                print(f"The total price of the shares is: {sellprice}")
                cash_balance = cash_balance + sellprice
                if stock in Portfolio:
                    Portfolio[stock] -= amount
                else:
                    Portfolio[stock] = -amount
                print(f"Your current portfolio consists of the following stock: {Portfolio}")
                print(f"Your current balance is now: {cash_balance}")


    # 6. Compare (e.g. cash balance or portfolio) to other users




    # 7. Exit






