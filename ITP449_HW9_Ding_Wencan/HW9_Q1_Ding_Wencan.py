# Ding Wencan
# ITP 449 Spring 2022
# HW9
# Q1
# Create a DataFrame “diabetes_knn” to store the diabetes data and set option to display
# all columns without any restrictions on the number of columns displayed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
diabetes_knn = pd.read_csv("diabetes(1).csv")
pd.set_option("display.max_columns", None)

# Determine the dimensions of the “diabetes_knn” dataframe
print("The dimension is", diabetes_knn.ndim)

# Update the DataFrame to account for missing values
diabetes_knn.fillna(0)


# Create the Feature and Target Vector
# Standardize the attributes of Feature Matrix
X = diabetes_knn.iloc[:,:-1]
y = diabetes_knn.iloc[:,-1]
for i in diabetes_knn.columns.values:
    X.loc[X[i]== 0,i] = round(X.loc[diabetes_knn[i]!= 0,i].mean())
myScaler = StandardScaler()
myScaler.fit(X)
X_Scaled = pd.DataFrame(myScaler.transform(X), columns=X.columns)
# Split the Feature Matrix and Target Vector into train A (70%) and train B sets (30%).
# Use random_state=2022, and stratify based on Target vector
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_Scaled,y,test_size=0.3,random_state=2022,stratify=y_train)
# Develop a KNN based model and obtain KNN score (accuracy) for train A and train B
# data for k’s values ranging between 1 to 8.
neighbors = np.arange(1,9)
trainA_Accuracy = []
trainB_Accuracy = []

for k in neighbors:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_trainA, y_trainA)
    y_predA = model.predict(X_trainA)
    y_predB = model.predict(X_trainB)
    trainA_Accuracy.append(metrics.accuracy_score(y_trainA, y_predA))
    trainB_Accuracy.append(metrics.accuracy_score(y_trainB, y_predB))

# Plot a graph of train A and train B score and determine the best value of k
plt.plot(neighbors, trainA_Accuracy, "--r", label="Train A")
plt.plot(neighbors, trainB_Accuracy, label="Train B")
plt.xlabel("# of neighbors(k)")
plt.ylabel("Accuracy")
plt.legend()
plt.xticks(neighbors)
plt.show()
print("The best value for k is 1")

# Display the score of the model with best value of k. Also print and plot the confusion
# matrix for Train B, using Train A set as the reference set for training
model = KNeighborsClassifier(n_neighbors =4)
model.fit(X_trainA, y_trainA)
y_pred_test = model.predict(X_trainB)
print("Accuracy on the test set:", metrics.accuracy_score(y_trainB, y_pred_test))
print(metrics.confusion_matrix(y_trainB,y_pred_test))
metrics.plot_confusion_matrix(model, y_trainB, y_pred_test)
plt.show()

# Predict the Outcome for a person with 6 pregnancies, 140 glucose, 60 blood pressure, 12
# skin thickness, 300 insulin, 24 BMI, 0.4 diabetes pedigree, 45 age.
input = [[6,140,60,12,300,24,0.4,45]]
output = model.predict(input)
print("The outcome is", output)