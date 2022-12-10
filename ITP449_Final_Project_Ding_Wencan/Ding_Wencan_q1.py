# Ding Wencan
# q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
# Load the data from the file
df = pd.read_csv("winequality(1).csv")
# Standardize all variables other than Quality(use StandardScalar)
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
myScaler = StandardScaler()
myScaler.fit(X)
X_Scaled = pd.DataFrame(myScaler.transform(X), columns=X.columns)
print(X_Scaled)
# Partition the dataset(Use random_state = 2022, Partitions 60/20/20, stratify = y
X_train, X_test, y_train, y_test = train_test_split(X_Scaled, y, test_size=0.2, random_state=2022, stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_train, y_train, test_size=0.25, random_state=2022, stratify=y_train)
# Build a KNN classification model to predict Quality based on all the remaining numeric variables
# Iterate on K ranging from 1 to 30. Plot the accuracy for the train A and train B datasets
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
plt.plot(neighbors, trainA_Accuracy, "--r", label="Train A")
plt.plot(neighbors, trainB_Accuracy, label="Train B")
plt.xlabel("# of neighbors (k)")
plt.ylabel("Accuracy")
plt.legend()
plt.xticks(neighbors)
plt.show()
# Which value of k produced the best accuracy in the train A and train B data sets
print("k = 18, produced the best accuracy in the train A and train B")
# Generate predictions for the test partition with the chosen value of K
# Print and plot the confusion matrix of the actual vs predicted wine quality
model = KNeighborsClassifier(n_neighbors=18)
model.fit(X_trainA, y_trainA)
y_pred_test = model.predict(X_test)
print("Here is the confusion matrix: ", metrics.confusion_matrix(y_test, y_pred_test))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred_test)
plt.show()
# Print the test dataframe with the added columns "Quality" and "Predicted Quality"
test = X_test
test["Quality"] = y_test
test["Predicted Quality"] = y_pred_test
print("Here is the test dataframe with the added columns:",test)
# Print the accuracy of model on the test dataset
print("Accuracy on the Test set:", metrics.accuracy_score(y_test, y_pred_test))

