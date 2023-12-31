# -*- coding: utf-8 -*-
"""ElectionStrategy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XTe_0u4lR5Gq_2aVlNz5YjqXxbkVwfMb
"""



import pandas as pd

# Read the CSV file into a Pandas DataFrame
nelly = pd.read_csv('/content/VotersData.csv')

# Print the shape of the dataset
print("Shape of the dataset:", nelly.shape)

# Print the first 5 rows of the dataset
nelly.head(11)

import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Load the dataset
nelly = pd.read_csv('VotersData.csv')

# Split the data into features (X) and labels (y)
X = nelly.drop("candidate_preference", axis=1)

y=nelly['candidate_preference']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

geo = DecisionTreeClassifier(criterion='entropy', random_state=42)
geo.fit(X_train, y_train)

# make predictions on the test data
y_pred = geo.predict(X_test)
print(y_pred)

# Calculate the accuracy of the decision tree classifier.
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy, confusion matrix, and classification report.
print('Accuracy:', accuracy)

# Alternatively use the code below:

print(f"Accuracy: {accuracy:.2f}")

# Evaluate the model's performance

report = classification_report(y_test, y_pred)
print("Classification Report:")

print(report)

conf_matrix = confusion_matrix(y_test, y_pred)

print("Confusion Matrix: ")
print(conf_matrix)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))


# Plot the decision tree
plot_tree(geo, filled=True, feature_names=X.columns, class_names=["Hillary Clinton", "Bernie Sanders", "Donald Trump", "Ted Cruz", "Donald Trump"])

# Display the plot
plt.show()

import joblib
geo = DecisionTreeClassifier(random_state=42)
geo.fit(X_train, y_train)
joblib.dump(geo, 'decision_tree_model.pkl')

import joblib
import pandas as pd
# load the saved model
loaded_model = joblib.load ('decision_tree_model.pkl')
# Prepare your new data with attribute names
new_data = pd.DataFrame({

    'voter_id': [1, 2, 3, 4],
    'age': [35, 42,65,52],
    'followers': [5000, 1358, 8500, 9356],
    'friends':[7509, 1200, 8500, 9356],
    'likes':[9000, 5009, 4500, 11007],
    'shares': [1457,124, 3987, 2357],
    'comments':[987,98, 345, 292]

})

import joblib
import pandas as pd

# Load the model
loaded_model = joblib.load('decision_tree_model.pkl')

# Prepare your new data with attribute names
new_data = pd.DataFrame({
    'voter_id': [1, 2, 3, 4],
    'age': [35, 28, 42, 32],
    'followers': [5000, 1358, 8500, 9356],
    'friends': [7509, 1200, 8500, 9356],
    'likes': [9000, 5009, 4500, 11007],
    'shares': [1457, 124, 3987, 2357],
    'comments': [987, 98, 345, 292]
})

# Make predictions on the new data
predictions = loaded_model.predict(new_data)

# Print the predictions as strings
for i, prediction in enumerate(predictions):
    print(f"Data {i+1}: Predicted Outcom - {prediction}")