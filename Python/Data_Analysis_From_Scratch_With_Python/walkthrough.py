#! Python3
# A walkthrough of the book "Data Analysis From Scratch With Python"

'''
# A Program which predicts species of an Iris flower based on lengths and width of its sepals
# and petals.

# Importing the necessary libraries
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

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
