#! Python3
# A walkthrough of the book "Data Analysis From Scratch With Python"

from sklearn.datasets import load_iris
from sklearn import tree, datasets, linear_model
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

'''
# A Program which predicts species of an Iris flower based on lengths and width of its sepals
# and petals.

# Loading Iris dataset
iris = load_iris()

x = iris.data  # Array of the data
y = iris.target  # Array of labels (i.e answers) of each data entry

# Getting label names i.e the three flower species
y_names = iris.target_names

# Taking random indices to split the dataset into train and test
test_ids = np.random.permutation(len(x))

# Splitting data and labels into train and test
# Keeping last 10 entries for testing, the rest for training

x_train = x[test_ids[:-10]]
x_test = x[test_ids[-10:]]

y_train = y[test_ids[:-10]]
y_test = y[test_ids[-10:]]

# Classifying using decision tree
clf = tree.DecisionTreeClassifier()

# Training (fitting) the classiiifier with the training set
clf.fit(x_train, y_train)

# Predictions on the test dataset
pred = clf.predict(x_test)

print(pred)  # Predicted labels i.e flower species
print(y_test)  # Actual labels
print((accuracy_score(pred, y_test))*100)  # Prediction accuracy
'''

'''
# A simple demo of a horizontal bar chart

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Marcus', 'Olivia', 'Luna', 'Bebisen', 'Miso', 'Daisy')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error,
        align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast did you go today?')

plt.show()
'''

'''
# Simple demo of a scatter plot chart

# Example random data
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()
'''

'''
# A linear regression demo

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_Y_train = diabetes.target[:-20]
diabetes_Y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_Y_train)

# Make predictions usinng the testing set
diabetes_Y_pred = regr.predict(diabetes_X_test)

# The coefficient
print('Coefficients:\n', regr.coef_)
# The mean squarded error
print('Mean squared error: %.2f' %
      mean_squared_error(diabetes_Y_test, diabetes_Y_pred))
# Explain variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_Y_test, diabetes_Y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_Y_test, color='black')
plt.plot(diabetes_X_test, diabetes_Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
'''
