# Problem 2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
# Read the dataset into a dataframe.
df = pd.read_csv("Titanic(1).csv")
pd.set_option("display.max_columns", None)
# Explore the dataset and determine what is the dependent variable.
print("The dependent variable is Survivied.")
# Drop factor(s) that are not likely to be relevant for a classification tree
df.drop(columns="Passenger",inplace=True)
# Make sure there are no missing values
print(df.isnull().values.any())
print("There are no missing values")
# Plot count plots of each of the remaining factors
sns.countplot(x="Class",data=df)
plt.title("Countplot for class")
plt.show()
sns.countplot(x="Age",data=df)
plt.title("Countplot for age")
plt.show()
sns.countplot(x="Sex",data=df)
plt.title("Countplot for sex")
plt.show()
# Convert all categorical variables into dummy variables
df1 = pd.get_dummies(df,drop_first=True)
#
X = df1.iloc[:,:-1]
y = df1.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
# Fit the training data to a classification tree. Display the classification tree.
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
plt.figure(figsize=(25,25))
fn = X.columns
cn = ("0","1")
tree.plot_tree(dt, feature_names=fn, class_names=cn,filled=True)
plt.show()
# Determine the accuracy of your predictions for survivability
y_pred = dt.predict(X_test)
print("Accuracy =", metrics.accuracy_score(y_test, y_pred))
# Determine the confusion matrix
print(metrics.confusion_matrix(y_test,y_pred))
# Now, display the predicted value of the survivability of a male adult in 3rd class
sample =[[0,1,0,1,0]]
print("The predicted value of survivability is", dt.predict(sample))