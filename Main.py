from StockData import requesting_one_stock

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
stock=input("Please select a stock: ")

# 4.b Show changes in stock through a time period (day, week, month, year) with %
datastock = requesting_one_stock(stock)
currentprice = datastock["close"][0]
# Buy stocks
decision = input(f"Do you want buy {stock} for {currentprice}? (yes/no)")
if decision == "yes":
    amount = int(input("How many stocks do you want to buy?"))
    costs = amount * currentprice
    cash_balance = cash_balance - costs
    Portfolio[stock] = amount
    print(Portfolio)
    print(costs)
    print(cash_balance)
# Sell stocks
# Compare (e.g. cash balance or portfolio) to other users
# Exit






