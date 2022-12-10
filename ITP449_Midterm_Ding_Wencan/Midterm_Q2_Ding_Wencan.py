# Ding Wencan
# Question2
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
# read csv
df = pd.read_csv("AAPL(1).csv")
# convert date to datetime and set index to date
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date",inplace=True)
# The difference
lowest = df.sort_values(["Low"], ascending =1)["Low"].head(1).values[0]
highest = df.sort_values(["High"], ascending =0)["High"].head(1).values[0]
difference = highest - lowest
print("The difference is",difference)
# How many days it took for Apple stock to reach its highest value since it hit its lowest value during this period
low = df.sort_values(["Low"], ascending=1).head(1)
high = df.sort_values(["High"],ascending=0).head(1)
date_df = high.index-low.index
print("How many days it took for Apple stock to reach its highest value since it hit its lowest value during this period?")
print(date_df)
# How many shares it took
print("How many shares of Apple (Volume) were traded during the day that it hit its highest price?")
print(high["Volume"][0])
# Plot the price of Apple Stock vs Time
plt.subplot(2,1,2)
plt.plot(df.index,df["Close"],label="Close Price")
plt.xlabel("Time")
plt.ylabel("Price")
# Plot the 20-Day Moving
smoothing = df["Close"].rolling(20).mean()
plt.subplot(2,1,1)
plt.plot(df.index,smoothing,label="20-Day-Moving-Average Close Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
