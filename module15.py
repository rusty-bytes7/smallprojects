#this is for module 15, regression analysis
import matplotlib.pyplot as plot
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


#open file
df = pd.read_csv('/Users/ericawolf/vscode/flights_1000.csv')

#Construct a linear regression model to predict ArrDelay values based on DepDelay values.
#make depdelay and arrdelay their own matrices

depdelay = df['DepDelay'] #p
arrdelay = df['ArrDelay'] #q

depdelay = np.array(depdelay).reshape((1000, 1))
arrdelay = np.array(arrdelay).reshape((1000, 1))

#make an empty regression
linreg = LinearRegression()

#teach the model based on arr and dep
linreg.fit(depdelay, arrdelay)

#calculate w1
print(linreg.coef_)

#calcuylate w0
print(linreg.intercept_)

#get preduictions
predicted_arrdelay = linreg.predict(depdelay)

# Use arrdelay and predicted arrdelay to plot red points. 
# Draw a diagonal green line.
# If a point shows on the green line exactly, that means 100% accurate prediction. 
# That is, predicted value is equal to real value. 
plot.plot(arrdelay, predicted_arrdelay, 'ro')
plot.plot([0, 150], [0, 150], 'g-')
plot.xlabel('real values')
plot.ylabel('predicted values')

#calculate the mean absolute error
print(mean_absolute_error(arrdelay, predicted_arrdelay))


