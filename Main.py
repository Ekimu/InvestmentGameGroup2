from StockData import requesting_one_stock

# Log in

# Show cash balance
print("Welcome to our Investment Game!!")
cash_balance = 10
print(f"Your starting balance is {cash_balance} USD")

# 3.a Show portfolio
#1st draft of portfolio structure
Portfolio = [

]
# Portfolio = [
#     { 'name': 'IMB', 'buyingprice': 2, 'stock': 100 },
#     { 'name': 'AMZN', 'price': 3, 'stock': 40 },
#     { 'name': 'cheese', 'price': 3, 'stock': 30 },
#     { 'name': 'milk', 'price': 1, 'stock': 80 }
# ]

# 3.b Show changes in portfolio through a time period (day, week, month, year) with %

# 4.a Search stock (based on stock symbol, names, market, currency, etc.)
print("Here is a list of some common stocks:")
print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
print("You can choose any stock you want.")
stock=input("Please select a stock: ")

# 4.b Show changes in stock through a time period (day, week, month, year) with %
requesting_one_stock(stock)

# Buy stocks
input(f"Do you want buy {stock} for PRICE? (b/s/no)")

# Sell stocks
# Compare (e.g. cash balance or portfolio) to other users
# Exit






