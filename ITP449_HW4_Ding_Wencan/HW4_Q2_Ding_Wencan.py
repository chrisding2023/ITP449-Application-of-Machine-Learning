# Wencan Ding
# ITP449 Spring 2022
# HW4
# Q2
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("data.csv")
plt.plot(df["Year"], df["Value"], marker ="o", linestyle ="--", color="red")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly")
plt.title("Global temperature")
plt.show()
