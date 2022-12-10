# Ding Wencan
# ITP449 Spring2022
# HW5
# Question3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data = pd.read_csv("02-22-2022.csv")
deaths = pd.read_csv("time_series_covid19_deaths_US.csv")
confirmed = pd.read_csv("time_series_covid19_confirmed_US.csv")

# What state in the US currently has the highest number of deaths?
print("What state in the US currently has the highest number of deaths?")
print(data.sort_values("Deaths",ascending=0)[["Province_State","Deaths"]].head(1))

# Which state in the US has the 2nd lowest incident rate (cases per 100,000 persons)?
print("Which state in the US has the 2nd lowest incident rate (cases per 100,000 persons)?")
df = data.sort_values("Incident_Rate")
print(df.iloc[1]["Province_State"])

# What is the difference in the testing rate between the state that tests the most and the state that tests the least?
print("What is the difference in the testing rate between the state that tests the most and the state that tests the least?")
test_most = data.loc[data["Total_Test_Results"] == max(data["Total_Test_Results"])]
test_least = data.loc[data["Total_Test_Results"] == min(data["Total_Test_Results"])]
print(test_most["Testing_Rate"].values[0]-test_least["Testing_Rate"].values[0])

#Plot the number of daily new cases in the US for the top 5 states with the highest confirmed cases (as of today). From March 1 – today. Use Subplot 1.
#Plot the number of daily deaths in the US for the top 5 states with the highest confirmed cases (as of today). From March 1 – today. Use Subplot 2.
confirmedcases = data.sort_values("Confirmed",ascending=0)
states = confirmedcases["Province_State"].head(5)
state = []
for s in states:
    state.append(s)
dates = pd.date_range("3/1/21", "2/22/22")
NewYork_D = deaths.loc[deaths["Province_State"]=="New York"].sum()[416:]
California_D = deaths.loc[deaths["Province_State"]=="California"].sum()[416:]
Texas_D = deaths.loc[deaths["Province_State"]=="Texas"].sum()[416:]
Florida_D = deaths.loc[deaths["Province_State"]=="Florida"].sum()[416:]
Illinois_D = deaths.loc[deaths["Province_State"]=="Illinois"].sum()[416:]

NewYork_C = confirmed.loc[confirmed["Province_State"]=="New York"].sum()[415:]
California_C = confirmed.loc[confirmed["Province_State"]=="California"].sum()[415:]
Texas_C = confirmed.loc[confirmed["Province_State"]=="Texas"].sum()[415:]
Florida_C = confirmed.loc[confirmed["Province_State"]=="Florida"].sum()[415:]
Illinois_C = confirmed.loc[confirmed["Province_State"]=="Illinois"].sum()[415:]

myFig = plt.figure(figsize=(15, 10), dpi=80)

ax1 = myFig.add_subplot(2, 1, 2)
ax2 = myFig.add_subplot(2, 1, 1)

ax1.plot(dates, NewYork_D, color="green",label="New York")
ax1.plot(dates, California_D, color="red",label="California")
ax1.plot(dates, Texas_D, color="blue",label="Texas")
ax1.plot(dates, Florida_D, color="yellow",label="Florida")
ax1.plot(dates, Illinois_D, color="purple",label="Illinois")
ax1.set_xlabel("Dates")
ax1.set_ylabel("Cumulative Death")
ax1.set_title("Number of daily deaths")
ax1.legend()
ax2.plot(dates, NewYork_C, color="green",label="New York")
ax2.plot(dates, California_C, color="red",label="California")
ax2.plot(dates, Texas_C, color="blue",label="Texas")
ax2.plot(dates, Florida_C, color="yellow",label="Florida")
ax2.plot(dates, Illinois_C, color="purple",label="Illinois")
ax2.set_xlabel("Date")
ax2.set_ylabel("Cumulative new cases")
ax2.set_title("Number of daily new cases")
ax2.legend()

plt.show()