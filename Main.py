from StockData import requesting_one_stock
print("Welcome to our Investment Game!!")
cash_balance = 10
print(f"Your starting balance is {cash_balance} USD")
print("Here is a list of some common stocks:")
print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
print("You can choose any stock you want.")
stock=input("Please select a stock: ")
input(f"Do you want buy or sell {stock} for PRICE? (b/s/no)")


requesting_one_stock(stock)