import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plot

test = pd.read_csv('/Users/ericawolf/vscode/testdigits.csv')
training = pd.read_csv('/Users/ericawolf/vscode/trainingdigits.csv')

print('The length of the test data is:',len(test))
print('The length of the training data is:', len(training))
