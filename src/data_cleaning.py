import pandas as pd 

# read data
data = pd.read_csv("data/Bitstamp_BTCUSD_d.csv")

# change data type
data["date"] = pd.to_datetime(data["date"])

# filter by date and choose close price of daily candle as the actual price
data = data[(data.date)>='2016-01-01'][['date','close']].sort_values('date',ascending=True)

# sort by date, ascending
data = data.sort_values('date').reset_index(drop=True)
data['Id'] = data.index + 1

# save cleaned data
data.to_csv("data/cleaned.csv",index=True)