import pandas_datareader as web

stocks=[]
my_file=open("symbols.txt","r")
for line in my_file:
    stocks.append(line.strip())

my_file.close()

web.DataReader(stocks,"yahoo",start="2000-1-1",end='2020-8-27')["Adj Close"].to_csv("prices.csv")
web.DataReader(stocks,"yahoo",start="2000-1-1",end='2020-8-27')["Volume"].to_csv("volume.csv")
