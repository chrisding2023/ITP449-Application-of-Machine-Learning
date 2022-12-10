# Wencan Ding
# ITP449 Spring 2022
# HW3
# Question1
#1
import pandas as pd
import numpy as np
DC = {"attempts":["1","3","2","3","2","3","1","1","2","1"] ,
      "name":["Anastasia","Dima","Katherine","James","Emily","Michael","Matthew","Laura","Kevin","Jonas"],
      "qualify":["yes","no","yes","no","no","yes","yes","no","no","yes"],
      "score":["12.5","9.0","16.5",np.nan,"9.0","20.0","14.5",np.nan,"8.0","19.0"]}#create a dictionary
df = pd.DataFrame(DC)#define a DataFrame
print(df)#print dataframe

#2
df1 = df.loc[df["qualify"]=="yes"][["name","attempts"]]
print(df1)#names + attempts of qualified contestants

#3
df2 = df.loc[(df["qualify"]=="yes") & (df["attempts"]=="1")][["name","score"]]
print(df2)#names and the score of contestants who qualified with a single attempt

#4
df3 = df.fillna(0)# replace NaN values with zeros
print(df3)

#5
df4 = df.sort_values(["attempts","score"], ascending=[True, False], inplace=False)
print(df4)
