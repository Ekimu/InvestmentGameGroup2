import requests
import pandas as pd

def requesting_one_stock(stock):
    # Requesting one stock from IBM, to see how it works :)
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=60min&apikey=KKM3IZ0WUPZTREAK&outputsize=full")

    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)

    # The service sends JSON data, we parse that into a Python datastructure
    raw_data = response.json()

    try:
        data = raw_data['Time Series (60min)']
        df = pd.DataFrame(data).T.apply(pd.to_numeric)
        #df.info()
        #print(df.head())
        return df
    except KeyError:
        print("Oops! That was not a stock name. Try again...")
        return None

