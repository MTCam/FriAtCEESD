import numpy as np
import matplotlib.pyplot as plt
import matplotlib

data = np.loadtxt('mirgecom_weak_3.txt')

fontsize = 16
params = {'text.usetex': True,
          'text.latex.preamble': r"""
                                  \usepackage{cmbright}
                                  """,
          'axes.labelsize': fontsize,
          'font.size': fontsize,
          'axes.titlesize': fontsize,
          'legend.fontsize': fontsize,
          'xtick.labelsize': fontsize,
          'ytick.labelsize': fontsize,
          }
matplotlib.rcParams.update(params)

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(data[:, 0], data[:, 1]/9, 'o-', lw=2, markerfacecolor='w', ms=6, markeredgewidth=2)

ax.set_xscale('log', base=2)
ax.set_ylim([0, 5])
ax.grid(True, axis='y', color='0.8')
ax.set_xticks(data[:,0])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_ylabel('WallTime/Timestep (s)')
ax.set_xlabel('Number of GPUs')
plt.title('Bozzle Eager on Lassen')
plt.savefig('gpuscaling.pdf', bbox_inches='tight')
