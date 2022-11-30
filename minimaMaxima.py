# Logic to find local minima and maxima in relevant dataset


# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema

# Read in traffic data from CSV file

df1 = pd.read_csv(r'C:\Users\janis.alltag\OneDrive - Basler & Hofmann\Desktop\Projekte\Albispass_COde\TimeSync\NoiseTime.csv', sep=';')

# just to test whether format is right:
print(df1["Laeq"])


# Find local peaks

n = 16  # variable for number of points to be checked before and after - I chose 16 values: each step = 125ms, therefore 16 = 2s.

df1['min'] = df1.iloc[argrelextrema(df1.Laeq.values, np.less_equal,
                    order=n)[0]]['Laeq']
df1['max'] = df1.iloc[argrelextrema(df1.Laeq.values, np.greater_equal,
                    order=n)[0]]['Laeq']

# Plot results

plt.scatter(df1.index, df1['min'], c='r')
plt.scatter(df1.index, df1['max'], c='g')
plt.plot(df1['Laeq'])
plt.show()