# Problem 3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from yellowbrick.regressor import ResidualsPlot
# Read the csv file using Pandas. Store the output into a dataframe frame
df = pd.read_csv("mtcars(2).csv")
pd.set_option("display.max_columns", None)
# Print the dataframe
print(df)
# You notice that the index is 0…31. There is a column Car Name. Set the index of the
# dataframe to the Car Name. In other words, make the column Car Name the index
# of frame
# Print frame
df.set_index("Car Name",inplace=True)
print(df)
# Create a statistical summary of the dataframe
print(df.describe())
# Produce a correlation matrix of all pairs of numerical variables. Which two numeric variables
# are most highly correlated? What is the correlation coefficient for the above pair?
print(df.corr())
print("disp and cyl are most highly correlated")
print("The correlation coefficient for the above pair is 0.902033")
# Create a scatterplot matrix of the numeric variables in the data. What do the figures in the
# diagonal going from the top left to the bottom right show?
sns.pairplot(df)
plt.show()
print("The figures in the diagonal show that the distribution of each variables against each other")
# For the pair in 6.a plot a scatterplot
model = LinearRegression(fit_intercept=True)
x = np.array(df["disp"])
y = np.array(df["cyl"])
X = x[:,np.newaxis]
model.fit(X,y)
y_predicted = model.predict(X)
plt.scatter(df["disp"],df["cyl"])
plt.plot(X,y_predicted,color="r")
plt.title("Scatterplot and Linear Regression of cyl vs displacement")
plt.ylabel("cyl")
plt.xlabel("displacement")
plt.show()
# Plot the residuals
X1 = df["disp"].values
X1 = X1.reshape(-1,1)
y1 = df["cyl"]
r = Ridge()
visualizer = ResidualsPlot(r)
visualizer.fit(X1,y1)
plt.title("Residuals for LinearRegression Model")
plt.ylabel("Residuals")
plt.show()