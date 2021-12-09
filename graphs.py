import requests
import pandas as pd

# Requesting one stock from IBM, to see how it works :)
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=KKM3IZ0WUPZTREAK")


# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

data = raw_data['Time Series (1min)']
df = pd.DataFrame(data).T.apply(pd.to_numeric)

#####added
df.index = pd.DatetimeIndex(df.index)
df.rename(columns=lambda s: s[3:], inplace=True)
#####end

df.info()
print(df.head())
########################################
#Used the code from StockData
#################

df[['open', 'high', 'low', 'close']].plot()