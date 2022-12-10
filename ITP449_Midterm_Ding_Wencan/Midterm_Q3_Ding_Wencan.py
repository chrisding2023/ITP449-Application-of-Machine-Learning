# Ding Wencan
# Question 3

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# Plot1
myFig = plt.figure(figsize= (14, 8))
ax1 = myFig.add_subplot(3,1,1)
ax2 = myFig.add_subplot(3,1,2)
ax3 = myFig.add_subplot(3,1,3)
x = np.random.randint(0,500,100)
y = np.random.normal(0,1,100)
ax1.scatter(x,y, marker="o",color="green")
ax1.set_ylabel("Random Nomral")
ax1.set_title("Scatter Chart")
# Plot2
a = np.arange(0,11,0.01)
b = np.sin(a)
ax2.plot(a,b,color="blue")
ax2.set_ylabel("SINE(X)")
ax2.set_title("Sine")
# Plot3
df = pd.read_csv("time_series_covid19(1).csv")
ax3.plot(df["Date"],df["US"],color="red",linewidth=6)
ax3.set_xlabel("Date")
ax3.set_ylabel("Cases")
ax3.set_title("US Covid-19 Cases")
ax3.set_xticks(["2/1/20","5/1/20","8/1/20","11/1/20","2/1/21","5/1/21","8/1/21"])
plt.show()




