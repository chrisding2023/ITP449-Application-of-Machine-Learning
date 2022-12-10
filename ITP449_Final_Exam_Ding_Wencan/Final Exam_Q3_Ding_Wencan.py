# Q3
# Ding Wencan
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
# 1.Create a DataFrame “ccDefaults” to store the credit card default data and set option to display all columns without any restrictions on the number of columns displayed. (2)
ccDeaults = pd.read_csv("ccDefaults(1).csv")
pd.set_option("display.max_columns", None)
# 2.Determine the number of non-null samples and feature data types
print("Whether there are missing values, the answer is", pd.isnull(ccDeaults).values.any())
print("There are no missing values")
print("The feature data types are\n")
print(ccDeaults.info())
# 3.Display the first 5 rows of ccDefaults.
print(ccDeaults.head())
# 4.Determine the dimensions of ccDefaults
print("The dimensions of dataframe is",ccDeaults.shape)
# 5.Drop the ‘ID’ column from ccDefaults
ccDeaults.drop("ID",inplace=True,axis=1)
# 6.Drop duplicates records from ccDefaults and identify if any duplicate records are dropped by printing out the dimensions of ccDefaults. (2)  Hint: ccDefaults.drop_duplicates(keep='first', inplace=True)
ccDeaults.drop_duplicates(keep="first",inplace=True)
print("After dropping the duplicates,")
print("The dimensions of dataframe is",ccDeaults.shape)
# 7.Print the correlation between all variable pairs
print("The correlation between all variable pairs are\n",ccDeaults.corr())
# 8.Create a Feature Matrix, including only the 4 most correlated variables with the target, and the Target Vector. (4) Hint: Look at the column of the target in the correlation matrix and see which features have the highest correlation with the target.
X = ccDeaults[["PAY_1","PAY_2","PAY_3", "PAY_4"]]
y = ccDeaults.iloc[:,-1]
# 9.Partition the data 70/30. (2) random_state=2022, stratify=y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=2022,stratify=y)
# 10.Develop Decision Tree Classifier model. (4)  criterion=‘entropy', max_depth=4, random_state=2022
dt = DecisionTreeClassifier(criterion="entropy",max_depth=4,random_state=2022)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
# 11.Display the accuracy of the model on the Test partition.
print("Accuracy of testing =", metrics.accuracy_score(y_test, y_pred))
# 12.Plot the confusion matrix
metrics.plot_confusion_matrix(dt, X_test, y_test)
plt.show()
# 13.Plot the decision tree
plt.figure(figsize=(25,25))
fn = X.columns
cn = list(map(str, dt.classes_.tolist()))
tree.plot_tree(dt, feature_names=fn, class_names=cn, filled=True)
plt.show()
