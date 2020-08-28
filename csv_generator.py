from pandas_datareader import data

stocks=[]
#my_file=open("symbols.txt","r")
#for line in my_file:
#    stocks.append(line.strip())

#my_file.close()

#df1=data.get_data_yahoo("AMZN",start="2000-1-1",end='2020-8-27')["Adj Close"]
#.to_csv("prices.csv")
df2=data.get_data_yahoo("AMZN",start="2000-1-1",end='2020-8-27')["Volume"]
#.to_csv("volume.csv")
print (df2)
#df1=web.DataReader(stocks,'yahoo',start="2000-1-1",end='2020-8-27')["Adj Close"].to_csv("prices.csv")
#df2=web.DataReader(stocks,'yahoo',start="2000-1-1",end='2020-8-27')["Volume"].to_csv("volume.csv")
