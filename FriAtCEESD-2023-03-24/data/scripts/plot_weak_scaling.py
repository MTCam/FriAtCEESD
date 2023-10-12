import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('mirgecom_weak_2.txt')
plt.plot(data[:, 0], data[:, 1]/9)
plt.xscale('log', base=2)
plt.ylim([0, 5])
plt.ylabel('WallTime/Timestep (s)')
plt.xlabel('Number of GPUs')
plt.show()
