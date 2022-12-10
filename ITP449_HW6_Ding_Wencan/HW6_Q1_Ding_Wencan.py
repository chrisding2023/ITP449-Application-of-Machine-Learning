# Ding Wencan
# ITP 499 Spring 2022
# HW6
# Q1
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
# Preparation
avocado = pd.read_csv("avocado.csv")
avocado = avocado[["Date","AveragePrice","Total Volume"]]
# Convert Data column to a timestamp using datetime
avocado["Date"] = pd.to_datetime(avocado["Date"])
print(avocado)

# 2.Plotting
myFig = plt.figure(figsize=(15, 10), dpi=80)
myFig.suptitle("Avocado Prices and Volume Time Series")
# Create a figure with 4 subplots
ax1 = myFig.add_subplot(2, 2, 1)
ax2 = myFig.add_subplot(2, 2, 2)
ax3 = myFig.add_subplot(2, 2, 3)
ax4 = myFig.add_subplot(2, 2, 4)
# Sort avocado by Date inplace in ascending order
avocado.sort_values("Date")
# Plot the average price of avocados over time in subplot1
ax1.scatter(avocado["Date"], avocado["AveragePrice"])
# Plot the total volume of avocados sold over time in subplot2
ax2.scatter(avocado["Date"], avocado["Total Volume"])
ax1.set_ylabel("Average Price")
ax2.set_ylabel("Total Volume")
# create a new column in avocado called TotalRevenue
avocado["TotalRevenue"] = avocado["AveragePrice"]*avocado["Total Volume"]
# create a new dataframe called avocado1
avocado1 = avocado.groupby("Date").sum()
# Recalculate the average price
avocado1["AveragePrice"] = avocado1["TotalRevenue"]/avocado1["Total Volume"]
# print the dataframe
print(avocado1)
# Plot the average price of avocado1 over time in subplot3
ax3.plot(avocado1["AveragePrice"])
# Plot the total volume of avocado1 sold over time in subplot4
ax4.plot(avocado1["Total Volume"])
ax3.set_ylabel("Average Price")
ax4.set_ylabel("Total Volume")
plt.show()
# 3.Plotting
# Plot the smoothed curve in subplot1 and 2.
plt.figure(figsize=(15, 10), dpi=80)
plt.title("Avocado Prices and Volume Time Series")
plt.subplot(1,2,1)
smoothing = avocado1["AveragePrice"].rolling(20).mean()
plt.plot(smoothing)
plt.ylabel("Average Price")
plt.subplot(1,2,2)
smoothing1 = avocado1["Total Volume"].rolling(20).mean()
plt.plot(smoothing1)
plt.ylabel("Total Volume")
plt.show()
