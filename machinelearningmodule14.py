import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plot

clf = tree.DecisionTreeClassifier()

test = pd.read_csv('/Users/ericawolf/vscode/testdigits.csv')
training = pd.read_csv('/Users/ericawolf/vscode/trainingdigits.csv')

#get length of data
print('The length of the test data is:',len(test))
print('The length of the training data is:', len(training))

#assign data to numpy array
testdata = test.to_numpy()
trainingdata = training.to_numpy()

#assign images to variable
number = testdata[0:1, 1:]
number.shape = (28,28)
plot.imshow(number,cmap = 'gray')