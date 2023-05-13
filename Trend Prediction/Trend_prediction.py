# -*- coding: utf-8 -*-
"""


@author: Ha Tran
Title: Trend_prediction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the source file
df = pd.read_csv("COVID19_case.csv")

plt.scatter(df.Date, df.Total_cases)

print (df.head)
x = np.arange(df['Date'].size)

fit = np.polyfit(x, df['Total_cases'], deg = 2)
print ("Slope : " + str(fit[0]))

#Fit function : y = mx + c [linear regression ]
fit_function = np.poly1d(fit)

#Linear regression plot
plt.plot(df['Date'], fit_function(x))
#Time series data plot
plt.plot(df['Date'], df['Total_cases'])

plt.title("COVID trend")
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()


# Source: https://ishan-mehta17.medium.com/simple-linear-regression-fit-and-prediction-on-time-series-data-with-visualization-in-python-41a77baf104c