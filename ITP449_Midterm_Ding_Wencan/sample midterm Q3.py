#Question3
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("mtcars.csv")# read csv and create a DataFrame using mtcars dataset
print(df)
# set the index of the dataframe to the Car Name
df.set_index("Car Name",inplace=True)
print(df)

# Create a DataFrame using attributes: ‘Car Name’, ‘cyl’, ’gear’, ‘hp’, ‘mpg’. Make Car Name the index. Rename the columns to: Cylinders, Gear, Horsepower, Miles Per Gallon. Print the DataFrame
df_new = pd.DataFrame(df,columns=["cyl","gear","hp","mpg"])
df_new.rename(columns={"cyl":"Cylinders","gear":"Gear","hp":"Horsepower","mpg":"Miles Per Gallon"},inplace =True)
print(df_new)

#3
print(df_new.sort_values(["Horsepower","Miles Per Gallon"],ascending=[0,1]))

#4
print(df_new.loc[df_new["Gear"]==4].sort_values(["Horsepower","Miles Per Gallon"],ascending=[0,1]))

#5
print(df_new.loc[df_new["Miles Per Gallon"]>20].count()[0])

#6
#a
plt.subplot(2,2,1)
plt.scatter(df_new["Horsepower"],df_new["Miles Per Gallon"])
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon")

#b
plt.subplot(2,2,2)
plt.hist(df_new["Cylinders"])
plt.xlabel("Cylinders")
plt.ylabel("Frequency")

#c
df2 = pd.read_csv("mtcars.csv")
plt.subplot(2,2,3)
plt.bar(x=df2["Car Name"],height=df_new["Gear"])
plt.ylabel("Gears")
plt.xticks(rotation=90)

#d
plt.subplot(2,2,4)
plt.boxplot(df_new["Horsepower"],showbox=True)
plt.ylabel("Horsepower")
plt.show()