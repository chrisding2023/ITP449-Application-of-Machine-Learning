# Ding Wencan
# q3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
import numpy as np
pd.set_option("display.max_columns", None)
df = pd.read_csv("UniversalBank(1).csv")
# What is the target variable?
print("The target variable is Personal Loan")

# Ignore the variable Row and Zip code
df.drop(columns=["Row","ZIP Code"],inplace=True)
print(df)
# Partition the data 75/25, random_state =2022, stratify= y
X = df[["Age","Experience","Income","Family","CCAvg","Education","Mortgage","Securities Account","CD Account","Online","CreditCard"]]
y = df["Personal Loan"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2022, stratify=y)
# How many of the cases in teh training partition represented people who accepted offer of a personal loan
print("In the training partition,", y_train.loc[y_train==1].count(),"of the cases represented who accepted offer of a personal loan")

# Plot the classification tree Use entropy creiterion max_depth=5,random_state=2022
dt = DecisionTreeClassifier(criterion="entropy",max_depth=5,random_state=2022)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)

plt.figure(figsize=(25,25))
fn = X.columns
cn = ("0","1")
tree.plot_tree(dt, feature_names=fn, class_names=cn,filled=True)
plt.show()
# On the testing partition, how many acceptors did the model classify as non-acceptors?
# On the testing partition, how many non-acceptors did the model classify as acceptors?

cf = metrics.confusion_matrix(y_test, y_pred)
print(cf)
metrics.plot_confusion_matrix(dt, X_test, y_test)
plt.show()
print("On the testing partition, 16 acceptors did the model classify as non-acceptors")
print("On the testing partition, 5 non-acceptors did the model classify as acceptors")
# What was the accuracy on the training partition?
# What was the accuracy on the test partition?
y_pred1 = dt.predict(X_train)
print("Accuracy of training =", metrics.accuracy_score(y_train, y_pred1))
print("Accuracy of testing =", metrics.accuracy_score(y_test, y_pred))
