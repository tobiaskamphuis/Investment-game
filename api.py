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
    return df.close

a = ['AAPL','AMZN','FB','GS','NFLX']

responses = {}
for stock_index in a:
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s" % (stock_index) + "&interval=5min&outputsize=full&apikey=31M2ZI1JW09RU5SA")
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    close_per_5min = bewerking(response)
    # print (close_per_5min)
    responses[stock_index] = close_per_5min
     # print(raw_data)

print (responses)

print (responses['AAPL'].loc['2019-11-13 09:35:00 '][0])

# print(responses.values([1]) #prints values
# print (responses)

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
