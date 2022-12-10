# Q1
# Ding Wencan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
# 1.Create a DataFrame “wineDf” to store the wine data.
wineDf = pd.read_csv("wineQualityReds(2).csv")
# 2.Determine the dimensions of the “wineDf” dataframe.
print("The dimensions for the dataframe is", wineDf.shape)
# 3.Check (and Update) the DataFrame to account for missing values
print("Whether there are missing values, the answer is", pd.isnull(wineDf).values.any())
print("There are no missing values")
# 4.Create the Feature Matrix and Target Vector
X = wineDf.iloc[:,1:-1]
y = wineDf.iloc[:,-1]
# 5.Standardize the attributes of Feature Matrix (use StandardScaler)
myScaler = StandardScaler()
myScaler.fit(X)
X_Scaled = pd.DataFrame(myScaler.transform(X), columns=X.columns)
# 6.Split the Feature Matrix and Target Vector into three partitions. Train A, Train B, and Test with the ratio of 50-25-25. (4)  random_state=2022, stratify=y
X_train, X_test, y_train, y_test = train_test_split(X_Scaled, y, test_size=0.25, random_state=2022,stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_train,y_train,test_size=0.33,random_state=2022,stratify=y_train)
# 7.How many cases are in the Train partition
print("The number of cases in the Train partition is",X_train.count()[0])
# 8.How many cases are in the Test partition
print("The number of cases in the Test partition is",X_test.count()[0])
# 9.Develop a kNN model based on Train A for various ks. k should range between 1 and 30.
# 10.Compute the kNN score (accuracy) for Train A and Train B data for those ks
neighbors = np.arange(1,31)
trainA_Accuracy = []
trainB_Accuracy = []
for k in neighbors:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_trainA, y_trainA)
    y_predA = model.predict(X_trainA)
    y_predB = model.predict(X_trainB)
    trainA_Accuracy.append(metrics.accuracy_score(y_trainA, y_predA))
    trainB_Accuracy.append(metrics.accuracy_score(y_trainB, y_predB))
# 11.Plot a graph of Train A and Train B accuracy and determine the best value of k. Label the plot
plt.plot(neighbors, trainA_Accuracy, "--r", label="Train A")
plt.plot(neighbors, trainB_Accuracy, label="Train B")
plt.xlabel("# of neighbors (k)")
plt.ylabel("Accuracy")
plt.legend()
plt.xticks(neighbors)
plt.show()
# 12.Now,using the selected value of k, score the Test data set
model = KNeighborsClassifier(n_neighbors=9)
model.fit(X_trainA, y_trainA)
y_pred_test = model.predict(X_test)
print("Accuracy on the Test set:", metrics.accuracy_score(y_test, y_pred_test))
# 13.Plot the confusion matrix (as a figure).
print("Here is the confusion matrix:\n", metrics.confusion_matrix(y_test, y_pred_test))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred_test)
plt.show()
# 14.What is the accuracy on the Train A partition?
y_predA = model.predict(X_trainA)
y_predB = model.predict(X_trainB)
print("Accuracy on the TrainA set:", metrics.accuracy_score(y_trainA, y_predA))
# 15.What is the accuracy on the Train B partition?
print("Accuracy on the TrainB set:", metrics.accuracy_score(y_trainB, y_predB))
# 16.Predict the wine quality of this wine
sample = [[8,0.6,0,2.0,0.067,10,30,0.9978,3.20,0.5,10.0]]
sample_scaled = pd.DataFrame(myScaler.transform(sample), columns=X.columns)
result = model.predict(sample_scaled)
print("The predicted quality for this wine is",result)