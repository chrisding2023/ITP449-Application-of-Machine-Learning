# Ding Wencan
# ITP 449 Spring 2022
# HW6
# Question2
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from yellowbrick.regressor import ResidualsPlot
df = pd.read_csv("CommuteStLouis.csv")
# create  a statistical summary of the data
print(df.describe())
plt.hist(df["Age"])
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Freq")
plt.show()
# produce a correlation matrix of age, distance and time
print(df.corr())
print("Time and distance are most highly correlated")
print("The correlation coefficient is 0.830241")
# create a scatterplot matrix of the numeric variables in the data
pd.plotting.scatter_matrix(df)
plt.show()
print("The diagonal plots show how each variable against themselves")
print("All three variables are right-skewed")
# produce a side-by-side boxplot of distance travelled by gender
sns.boxplot(x="Sex",y="Distance",data=df)
plt.show()
print("The data does not indicate that women tend to commute shorter distances")
# superimpose a linear regression line on plot 1
model = LinearRegression(fit_intercept=True)
x = np.array(df["Distance"])
y = np.array(df["Time"])
X = x[:,np.newaxis]
model.fit(X,y)
y_predicted = model.predict(X)
plt.scatter(df["Distance"], df["Time"])
plt.plot(x,y_predicted)
plt.title("Scatterplot and Linear Regression of Time vs Distance")
plt.ylabel("Time")
plt.xlabel("Distance")
plt.show()

# Show the distribution of residuals of the data from Question 3
x1 = df["Distance"].values
X1 = x1.reshape(-1,1)
y1 = df["Time"]
r = Ridge()
visualizer = ResidualsPlot(r)
visualizer.fit(X1,y1)

plt.title("Residuals for LinearRegression Model")
plt.ylabel("Residuals")
plt.show()



