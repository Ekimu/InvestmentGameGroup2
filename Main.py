from StockData import requesting_one_stock
print("Here is a list of some common stocks:")
print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
print("You can choose any stock you want.")
stock=input("Please select a stock: ")


requesting_one_stock(stock)