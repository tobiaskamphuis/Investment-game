import requests
import pandas as pd

#response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo")
#response = requests.get("https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&apikey=demo&symbols=MSFT,AAPL,FB")

def bewerking(response):
    raw_data = response.json()
    colname = list(raw_data.keys())[-1]
    data = raw_data[colname]
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    df.index = pd.DatetimeIndex(df.index)
    df.rename(columns=lambda s: s[3:], inplace=True)
    # print(df.head(78))
    return df.close

responses = {}
def getprices(symbol):
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s" % (symbol) + "&interval=5min&outputsize=full&apikey=31M2ZI1JW09RU5SA")
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    close_per_5min = bewerking(response)
    responses[symbol] = close_per_5min

# print (responses)
# print (responses['AAPL'].loc['2019-11-13 09:35:00 '][0])
# for a in responses['AAPL']:
#     print (a)
#
# print(responses[investment][:390].max())
# print(responses[investment][:390].idxmax())
# print(responses[investment][:390].idxmin())

def pricemax (investment):
    return responses[investment][:390].max()

def pricemin (investment):
    return responses[investment][:390].min()

def pricelatest (investment):
    return responses[investment][0]

#pricemax and pricelow are highest and lowest price in last 5 days (78 observations per day)

#
# pricemax = responses[investment][:390].max()
# pricemin = responses[investment][:390].min()
# pricelatest = responses[investment][0]
#
# print (pricemax)
# print (pricemin)
# print (pricelatest)

# print(responses[1].loc['2019-12-03 16:00:00 '][0])
# entry = responses[1].loc['2019-12-03 15:00:00 ']
# date = str(entry.index)
#
# # print (date)
# pairs = [(date,entry[0])]
# # print (pairs)
#
# stockdict = dict (pairs)
# print (stockdict)
#
# for entry in responses [1]:
#     date = str(entry.index)
#     values= responses[1].loc[date][0]
#     pairs = [date,values]
#     stockdict = dict (pairs)
#
# print (stockdict)



#         def  get_latest_price(self, stock):
#             stock_data = self._data[self._data["Symbol"] == stock]
#             return stock_data.iloc[0, 3]

# responses.append(requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s" % (stock_index) + "&interval=5min&outputsize=full&apikey=31M2ZI1JW09RU5SA"))
    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    # if responses.status_code != 200:
    #     raise ValueError("Could not retrieve data, code:", responses.status_code)
# stock_index = input ()

# print("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s" % (stock_index[3]) +"&interval=5min&outputsize=full&apikey=demo")
# def functie van de bewwerking


# # The service sends JSON data, we parse that into a Python datastructure
# raw_data = responses.json()
# raw_data.keys()
#
# print(raw_data)
#
# colname = list(raw_data.keys())[-1]
# data = raw_data[colname]
#
# df = pd.DataFrame(data).T.apply(pd.to_numeric)
# df.info()
# df.head()
#
# df.index = pd.DatetimeIndex(df.index)
# df.info
# df.rename(columns=lambda s: s[3:], inplace=True)
# df.head
# print (df.head)
#
# close_per_5min = df.close
# print (close_per_5min)
#
# #close_per_hour = df.close.resample('H').last()
# #print (close_per_hour)
