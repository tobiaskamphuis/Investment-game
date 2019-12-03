import requests
import pandas as pd
#response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo")
#response = requests.get("https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&apikey=demo&symbols=MSFT,AAPL,FB")
# #response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()
raw_data.keys()

print(raw_data)

colname = list(raw_data.keys())[-1]
data = raw_data[colname]

df = pd.DataFrame(data).T.apply(pd.to_numeric)
df.info()
df.head()

df.index = pd.DatetimeIndex(df.index)
df.info
df.rename(columns=lambda s: s[3:], inplace=True)
df.head
print (df.head)

close_per_5min = df.close
print (close_per_5min)

#close_per_hour = df.close.resample('H').last()
#print (close_per_hour)
