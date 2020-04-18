import pandas_datareader.data as web
import datetime
start = datetime.datetime(2019, 1, 1) # or start = '1/1/2016'
end = datetime.date.today()
prices = web.DataReader('AAPL', 'yahoo', start, end)
print(prices.head())
print(prices.info)
actions = web.DataReader('AAPL', 'yahoo-actions', start, end)
print(actions.head())