# Problem1
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# Create a DataFrame “diabetes_lr” to store the diabetes data and set option to display all
# columns without any restrictions on the number of columns displayed.
pd.set_option("display.max_columns", None)
df = pd.read_csv("diabetes(2).csv")
# Determine number of non-null samples and feature types.
print("The number of non-null samples is", pd.isnull(df).count()[0])
print(df.info())
# Display the first 5 rows of the "disbetes_Ir" dataframe
print(df.head())
# Print summary statistics (i.e. count, mean, … 75%, max
print(df.describe())
# Compute a correlation matrix depicting the relationship between attributes
print(df.corr())
# Determine how many diabetes positive and diabetes negative cases are present in the provided
# dataset
print("The number of positive cases is", df.loc[df["Outcome"] == 0]["Outcome"].count())
print("The number of negative cases is", df.loc[df["Outcome"] == 1]["Outcome"].count())
# Display the relationship between attributes in the dataset in a graphical format using seaborn’s
# pairplot()
sns.pairplot(df)
plt.show()
# Create the Feature Matrix and Target Vector
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
# Split the Feature Matrix and Target Vector into training and testing sets, reserving 25% of the
# data for testing. random_state = 2020
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2020)
# Develop a Logistic Regression model determine its accuracy on the train and the test data sets.
model = LogisticRegression()
model.fit(X,y)
y_pred = model.predict(X_test)
print("The accuracy is", metrics.accuracy_score(y_test, y_pred))
# Plot the confusion matrix
metrics.plot_confusion_matrix(model, X_test, y_test)
plt.show()
# Predict the diabetes diagnosis for a patient of your choice.
input = [[6,140,60,12,300,24,0.4,45]]
output = model.predict(input)
print("The outcome is", output)