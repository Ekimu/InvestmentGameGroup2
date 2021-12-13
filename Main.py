

# 3.a Search stock (based on stock symbol, names, market, currency, etc.)
# 3.b Show changes in stock through a time period (day, week, month, year) with %
while True:
    inspect=input("Would you like to inspect a stock: (y/n)")
    if inspect != "y":
        print("You decided not inspect any stock, we'll end here")
        break
    elif inspect == "y":



            buysell = input(f"Do you want to buy or sell {stock} for the current price {currentprice}? (b/s/n)")


        # 4. Buy stocks
            if buysell == "b":



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






