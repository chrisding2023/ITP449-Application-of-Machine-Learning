# Q2
# Ding Wencan
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# 1.Load the file and read the dataset into a dataframe.
df = pd.read_csv("Breast_Cancer.csv")
pd.set_option("display.max_columns", None)
# 2.Make sure there are no missing values
print("Whether there are missing values, the answer is", pd.isnull(df).values.any())
print("There are no missing values")
# 3.Explore the dataset and determine what the target variable is. Define the features based on all remaining columns
print("The target variable is", df.columns[0])
X = df.iloc[:,1:]
y = df.iloc[:,0]
# 4.Get a countplot of the target
sns.countplot(x="diagnosis", data=df)
plt.show()
# 5.Partition the data into train and test sets (75/25). Use random_state = 2022, startify = y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2022, stratify=y)
# 6.Fit the training data to a logistic regression model.
model = LogisticRegression()
model.fit(X_train, y_train)
# 7.Display the accuracy, precision and recall of your predictions for survivability. (4)
# Hint: use metrics.classification_report()
y_pred = model.predict(X_test)
print(metrics.classification_report(y_test, y_pred, labels=["B","M"]))
# 8.Print and plot the confusion matrix for the test set.
print("The confusion matrix for the test set is\n", metrics.confusion_matrix(y_test, y_pred))
metrics.plot_confusion_matrix(model, X_test, y_test)
plt.show()
