#! Python3

# A simple linear regression demo

# Importing the necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(
    'Data_Analysis_From_Scratch_With_Python//programs//Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0)

# Fitting simple linear regression to the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set result
y_pred = regressor.predict(X_test)

# Visualising the training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs. Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs. Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
