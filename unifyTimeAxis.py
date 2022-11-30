# Logic to unify the time axis between two datasets


# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read files with pandas, seperator commentary necessary, else semicolor error
df1 = pd.read_csv(r'C:\Users\janis.alltag\OneDrive - Basler & Hofmann\Desktop\Projekte\Albispass_COde\TimeSync\NoiseTime.csv', sep=';')
df2 = pd.read_csv(r'C:\Users\janis.alltag\OneDrive - Basler & Hofmann\Desktop\Projekte\Albispass_COde\TimeSync\TrafficTime.csv', sep=';')


# write time column to variables
df1['time'] = pd.to_datetime(df1['time'])
df2['time'] = pd.to_datetime(df2['time'])

# merge timelines together - parameter 1s necessary to get desired result
df_a = pd.merge_asof(df1, df2, on="time", tolerance=pd.Timedelta("1s"))


#with open(r'C:\Users\janis.alltag\OneDrive - Basler & Hofmann\Desktop\Projekte\Albispass_COde\Data\myfile.txt', 'w') as f:
#    for line in df_a:
#       f.write(f"{line}\n")

# Write merged timeline to file
df_a.to_csv('master.csv')

#test whether merge worked
print(df_a.loc[:, "time"])


#write columns into variables for use in matplotlib commands
x = df_a["time"]
y = df_a["Laeq"]
z = df_a["v"]

print(x[::8])


# plot desired results
xs = np.linspace(1, 21, 200)

plt.plot(x, y, color='g', linestyle='dashed', label="SPL")
plt.plot(x, z, color='r', linestyle='dashed', marker='o', label="Event")
plt.vlines(x=[x], ymin=z, ymax=len(xs), colors='black', ls='--', lw=0.25, label='traffic event')
plt.xticks(x=x[::8], rotation=90)
plt.xlabel("time")
plt.ylabel("SPL")
plt.legend()
plt.show()


