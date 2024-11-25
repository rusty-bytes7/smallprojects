import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plot

# Load data
test = pd.read_csv('/Users/ericawolf/vscode/testdigits.csv')
training = pd.read_csv('/Users/ericawolf/vscode/trainingdigits.csv')

# Get length of data
print('The length of the test data is:', len(test))
print('The length of the training data is:', len(training))

# Assign data to numpy arrays
testdata = test.to_numpy()
trainingdata = training.to_numpy()

# Assign images to variables
numbertest = testdata[0:1, 1:]
numbertraining = trainingdata[0:1, 1:]

# Change shape of data
numbertest.shape = (28, 28)
numbertraining.shape = (28, 28)

# Get counts for each number from original data
print('Test Numbers:\n', test['label'].value_counts())
print('Training Numbers\n', training['label'].value_counts())

# Train the model
xtrain = trainingdata[0:21000, 1:]
train_label = trainingdata[0:21000, 0]

# Create decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train data
clf.fit(xtrain, train_label)

# Prepare test data
testing = testdata[0:1000, 1:]
test_label = testdata[0:1000, 0]

# Predict the labels for test data
predicted_labels = clf.predict(testing)

# Accuracy assessment
accuracy = accuracy_score(test_label, predicted_labels)
print(f'Accuracy of the model: {accuracy * 100:.2f}%')

# Example of visualizing a test sample
test_number = np.array(testing[0])
test_number.shape = (28, 28)
plot.imshow(test_number, cmap='gray')
plot.show()

# Predict and print for a single test sample
print(f'Predicted label: {clf.predict(test_number.reshape(1, -1))}')
print(f'True label: {test_label[0]}')

# Predict the labels for the test data
predicted_labels = clf.predict(testing)

# Initialize counters for correct predictions and total occurrences
correct_counts = [0] * 10
total_counts = [0] * 10

# Compare predicted labels to true labels
for true, pred in zip(test_label, predicted_labels):
    total_counts[true] += 1
    if true == pred:
        correct_counts[true] += 1

# Calculate and print accuracy for each digit
print("Accuracy for each digit:")
for digit in range(10):
    if total_counts[digit] > 0:
        accuracy = correct_counts[digit] / total_counts[digit]
        print(f"Digit {digit}: {accuracy * 100:.2f}%")
    else:
        print(f"Digit {digit}: No samples in test set.")
