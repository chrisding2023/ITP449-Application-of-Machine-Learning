# Wencan Ding
# ITP449 Spring 2022
# HW3
# Question2
#1 read csv and print df
import pandas as pd
df = pd.read_csv("HW5/Trojans_roster.csv")
print(df)

#2 set index to #
df.set_index("#")
print(df)

#3 remove the "LAST SCHOOL" column
df = df.drop(columns="LAST SCHOOL")
print(df)

#4 print the names of all the Quarterbacks in the team
print(df.loc[df["POS."]=="QB","NAME"])

#5 print the name, position, height, and weight of the tallest player in the team
print(df.loc[df["HT."] == max(df["HT."]),["NAME","POS.","HT.","WT."]])

#6 print how many players are local
print(df.loc[df["HOMETOWN"]=="Los Angeles, CA"].count()[1])

#7 print the info of 3 heaviest players
print(df.sort_values("WT.", ascending=0).head(3))

#8 define a new column for BMI
df["BMI"] = 703*(df["WT."]/(df["HT."]**2))
print(df)

#9 print the mean and median of player's height, weight, and BMI
print(df[["HT.","WT.","BMI"]].mean())
print(df[["HT.","WT.","BMI"]].median())

#10 print the mean and median of players'height,weight,and BMI for each position
print(df.groupby("POS.")[["HT.","WT.","BMI"]].mean())
print(df.groupby("POS.")[["HT.","WT.","BMI"]].median())

#11 print the number of players in each position
print(df.groupby("POS.").count())

#12 print the names of the players whose BMI is below the team average
print(df.loc[df["BMI"]<(df["BMI"].mean())]["NAME"])

#13 print all the unique players' numbers
print(df["#"].unique())