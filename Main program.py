import pandas as pd
from StockData import requesting_one_stock
from graphs import creating_graph

cash_balance = 10000
cols=["Name", "buying_price", "amount", "value"]

Portfolio= pd.DataFrame(columns=cols)

# Portfolio = {
#         }
# Startup message / Log in
username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")
print(f"Welcome to our Investment Game, {username_input}!")

#Main program.py:
while True:
    print("""
    Main menu:
    1. Show current cash balance
    2. Show current portfolio
    3. Search for stocks
    4. Buy stocks
    5. Sell stocks
    6. Compare to other users
    0. Quit 
    """)
    choice=input("Please choose what you want to do: ")
    print("""
    """)
    if choice=="1":
        print("1. Show current cash balance")
        print(f"Your current balance is now: {cash_balance} USD")

    elif choice=="2":
        print("2. Show current portfolio")
        print(f"""Your current portfolio contains following stocks 
{Portfolio}""")
        Portfolio.groupby(["Name"]).sum("amount").sum("value")

        # 2.b Maybe option for looking at development in specific stocks in portfolio
        # totalvalue = 0
        # for stocks in Portfolio:
        #
        #     portfoliodata = requesting_one_stock(stocks)
        #     Portfolioprice = portfoliodata["4. close"][0]
        #     totalvalue += Portfolioprice * Portfolio[stocks]
        #     print(f"The current holdings of {stocks} amounts to {Portfolioprice*Portfolio[stocks]} USD.")
        # print(f"The current total value of your portfolio is {totalvalue} USD.")
        # print(f"Your current cash balance is now: {cash_balance} USD")


    elif choice=="3":
        print("3. Search for stocks")
        print("Here is a list of some common stocks:")
        print("Tesla (TSLA), Apple (AAPL), Amazon (AMZN), Microsoft (MSFT), Nio Limited (NIO), Nvidia (NVDA), Moderna (MRNA), Nikola (NKLA), IBM (IBM).")
        while True:
            stock = input("Please select a stock (symbol): ")
            datastock = requesting_one_stock(stock)
            if datastock is None:
                continue
            creating_graph(datastock, stock)
            break

    elif choice=="4":
        print("4. Buy stocks")
        while True:
            stock = input("Please select the stock you want to buy (symbol): ")
            datastock = requesting_one_stock(stock)
            if datastock is None:
                continue
            break
        currentprice = datastock["4. close"][0]

        while True:
            try:
                amount = int(input(f"How many shares do you want to buy of {stock}?: "))
                break
            except ValueError:
                print("Oops! Not a number. Try again... ")

        costs = amount * currentprice
        confirmbuy = input(f"Please confirm you want to buy {amount} shares of {stock} for the cost of {costs} USD? (y/n)" )
        if confirmbuy != "y":
            print("You chose not to buy any stocks. You'll be sent to main menu.")
        else:
            new_cash_balance = cash_balance - costs
            if new_cash_balance < 0:
                print("You don't have enough cash in your balance to buy this stock. You will be sent to the main menu.")
            else:
                cash_balance = new_cash_balance
                print(f"You bought {amount} shares of {stock} for the cost of {costs} USD, back to main menu you go!")
                newrow=[stock, currentprice, amount, currentprice*amount]
                newdf = pd.DataFrame([newrow], columns=cols)
                Portfolio=pd.concat([Portfolio, newdf])
                Portfolio.reset_index(inplace=True, drop=True)
                # if stock in Portfolio:
                #     Portfolio[stock] += amount
                # else:
                #     Portfolio[stock] = amount
    elif choice=="5":
        print("5. Sell stocks")
        while True:
            stock = input("Please select the stock you want to sell (symbol): ")
            datastock = requesting_one_stock(stock)
            if datastock is None:
                continue
            break
        currentprice = datastock["4. close"][0]

        while True:
            try:
                amount = int(input(f"How many shares do you want to sell of {stock}?: "))
                break
            except ValueError:
                print("Oops! Not a number. Try again... ")

        gains = amount * currentprice
        confirmsell = input(
            f"Please confirm you want to sell {amount} shares of {stock} for the total value of {gains} USD? (y/n)")
        if confirmsell != "y":
            print("You chose not to sell any stocks. You'll be sent to main menu.")
        else:
            sellscurrentamount = Portfolio[Portfolio['Name'] == stock]['amount'].sum()
            if sellscurrentamount < amount:
                print("You own less shares, than you want to sell of this stock. You will be sent to the main menu.")
            else:
               print(f"You sold {amount} shares of {stock} for the total value of {gains} USD, back to main menu you go!")
               newrow = [stock, currentprice, -amount, currentprice*(-amount)]
               newdf = pd.DataFrame([newrow], columns=cols)
               Portfolio = pd.concat([Portfolio, newdf])
               Portfolio.reset_index(inplace=True, drop=True)
               cash_balance = cash_balance + gains

            # if stock in Portfolio:
            #     if Portfolio[stock] < amount:
            #         print("You own less shares, than you want to sell of this stock. You will be sent to the main menu.")
            #     else:
            #        print(f"You sold {amount} shares of {stock} for the total value of {gains} USD, back to main menu you go!")
            #        Portfolio[stock] -= amount
            #        cash_balance = cash_balance + gains
            # else:
            #     print("You don't own this stock. You will be sent to the main menu.")

    elif choice=="6":
        print("6. Compare to other users")

    elif choice=="0":
        print("Thank you for playing our Investment Game. Hope to see you soon. Bye!")
        break
    else:
        print("Please choose from the list")
