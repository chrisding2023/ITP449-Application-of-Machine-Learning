# Ding Wencan
# ITP 449 Spring 2022
# HW7
# Q1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
# Read the dataset into a dataframe
df = pd.read_csv("Titanic.csv")
# Explore the dataset and determine what is the target variable
print("The target variable is survived, which is based on the other factors.")
# Drop factor that are not likely to be relevant for logistic regression
df_drop = df.drop(["Passenger"], axis=1)
# Make sure there are no missing values
df1 = df_drop.dropna()
# Plot count plots of each of the remaining factors
sns.countplot(x="Age", data=df1)#Age Plot
plt.show()
sns.countplot(x="Sex", data=df1)#Sex Plot
plt.show()
sns.countplot(x="Class", data=df1)#Class Plot
plt.show()
# Convert all categorical variables into dummy variables#
df2 = pd.get_dummies(df1,columns=df1.columns[0:3])
df2.drop(columns=df2.columns[[4,5,8]],inplace=True)
# Partition the data into train and test sets(75/25).Use random_state =2022
X = df2.iloc[:, 1:]
y = df2.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2022)
# Fit the training data to a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Display the accuracy, precision and recall of your predictions for survivability
print("The accuracy is", metrics.accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
# Display the confusion matrix along with the labels (Yes, No)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.plot_confusion_matrix(model, X_test, y_test)
plt.show()
# Display the predicted value of the survivability of an adult female passenger traveling 2 class
X_New = [[0, 1, 0, 0, 1]]
Y_New = model.predict(X_New)
print("The predicted value is", Y_New)