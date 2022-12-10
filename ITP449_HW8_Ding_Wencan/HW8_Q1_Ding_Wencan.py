# Ding Wencan
# ITP449 Spring 2022
# HW8
# Q1

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the dataset into a dataframe. Be sure to import the header
df = pd.read_csv("wineQualityReds(1).csv",header=0)

# Drop Wine from the dataframe
df.drop(columns="Wine",inplace=True)

# Extract Quality and store it in a separate variable
quality = df["quality"]

# Drop Quality from the dataframe
df.drop(columns="quality",inplace=True)

# Print the dataframe and Quality
print(df)
print(quality)

# Normalize all columns of the dataframe. Use the MinMAxScaler class from sklearn.preprocessing
Normal = MinMaxScaler()
Normal.fit(df)
df_n = pd.DataFrame(Normal.transform(df), columns= df.columns)

# Print the normalized dataframe
print(df_n)

# Create a range of k values from 1:21 for k-means clustering. Iterate on the k values and store the inertia for each clustering in a list
ks = range(1,21)
inertia = []
for k in ks:
    model = KMeans(n_clusters = k)
    model.fit(df_n)
    inertia.append(model.inertia_)

# Plot the chart of inertia vs number of clusters
plt.plot(ks, inertia, "-o")
plt.xlabel("# of cluster (k)")
plt.ylabel("Inertia")
plt.xticks(ks)
plt.show()

# What K (number of clusters) would you pick for k-means?
print("I would like to pick cluster 6")

# Now cluster the wines into K =6 clusters. Use random_state =2202 when you instantiate the k-means model. Assign the respective cluster number tgo each wine. Print the dataframe sghwoing the cluster number for each wine.
model = KMeans(n_clusters = 6,random_state=2022)
model.fit(df_n)
df_n["Cluster"] = pd.Series(model.labels_)
print(df_n)

# Add the quality back to the dataframe
df_n["quality"] = quality
print(df_n)

# Now print crosstab of cluster number vs quality. Commemt if the cluster represent the quality of wine
print(pd.crosstab(df_n["quality"],df_n["Cluster"]))
print("clusters does not represent the quality of wine")