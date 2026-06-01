# Naive Bayes Classifier for Smart Parking System

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from pathlib import Path
import config

# Importing the dataset using config path
dataset = pd.read_csv(config.TRAINING_DATA_PATH)

# Features: Distance to each slot (A,B,C,D) and prices for each slot
# Target: Slot (A, B, C, or D) - column index 12
X = dataset.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]].values  # Features
y = dataset.iloc[:, 12].values  # Target (Slot column)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print(f"Confusion Matrix:\n{cm}")

# Save the trained model using config path
pickle.dump(classifier, open(str(config.ML_MODEL_PATH), 'wb'))
print(f"Model saved to {config.ML_MODEL_PATH}")

# Test prediction
test_data = [[10, 50, 60, 70, 15, 20, 25, 30]]
prediction = classifier.predict(test_data)
print(f"Test Prediction: {prediction[0]}")