from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
# series = read_csv('ai_timeseries_20210908.txt', delim_whitespace=True, header=0)
data = np.loadtxt('ai_verif_data_20210910.txt')
plt.plot(data[:, 0], data[:, 1])
plt.xscale('log')
plt.ylabel('Temperature (K)')
plt.xlabel('Time (s)')
plt.show()
