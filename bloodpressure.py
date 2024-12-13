#this is a program to analyze my blood pressure data
import pandas as pd
import numpy as np
import math

#import file
df = pd.read_csv('/Users/ericawolf/vscode/smallprojects/bp_data.csv')

#print summary statistics
#systolic
sys = df['SYS(mmHg)']
sysmean = sys.mean().round(2)
sysmax = sys.max().round(2)
sysmin = sys.min().round(2)
print('Your overall average Systolic Measurement is:', sysmean)
print('Your maximum Systolic Measurement is:', sysmax)
print('Your minimum Systolic Measurement is:', sysmin, '\n')


#diastolic
dys = df['DIA(mmHg)']
dysmean = dys.mean().round(2)
dysmax = dys.max().round(2)
dysmin = dys.min().round(2)
print('Your overall average Diastolic Measurement is:', dysmean)
print('Your maximum Diastolic Measurement is:', dysmax)
print('Your minimum Diastolic Measurement is:', dysmin, '\n')

#pulse
pulse = df['Pulse(Beats/Min)']
pulsemean = pulse.mean().round(2)
print('Your overall average Pulse Measurement is:', pulsemean)

#plot data via line plot
df.plot(x='Date', y=['SYS(mmHg)', 'DIA(mmHg)'])