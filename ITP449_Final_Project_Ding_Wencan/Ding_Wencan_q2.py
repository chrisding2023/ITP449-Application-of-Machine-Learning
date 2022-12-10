# Ding Wencan
# q2
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# Perform the necessary data preparation for the stores dataframe
# Standardize the dataset
df = pd.read_csv("Stores.csv")
store = df["Store"]
df.drop(columns="Store",inplace=True)
Scaler = StandardScaler()
Scaler.fit(df)
df_n = pd.DataFrame(Scaler.transform(df),columns=df.columns)
# Run k-means for k ranging from 1 to 10 random_state=2022
# Plot the inertias vs k
ks = range(1,11)
inertia = []
for k in ks:
    model = KMeans(n_clusters=k, random_state=2022)
    model.fit(df_n)
    inertia.append(model.inertia_)
plt.plot(ks, inertia, "--o")
plt.xlabel("# of cluster (k)")
plt.ylabel("Inertia")
plt.xticks(ks)
plt.show()
# What is the best K?
print("The best K is 6")
# What cluster does this store belong to
model = KMeans(n_clusters=6, random_state=2022)
model.fit(df_n)
sample = [[6.3,3.5,2.4,0.5]]
sample_n = pd.DataFrame(Scaler.transform(sample),columns=df.columns)
print("The store belong to cluster", model.predict(sample_n)[0])

# Now add the "Store" column and cluster number to the Dataframe. Display the dataframe
df_n["Cluster"] = pd.Series(model.labels_)
df_n["Store"] = store
print(df_n)

# Plot a histogram of cluster number
plt.hist(df_n["Cluster"],bins=range(7),align="right")
plt.xticks(np.arange(1,7))
plt.xlabel("cluster number")
plt.ylabel("The number of items in cluster")
plt.show()