import matplotlib.pyplot as plt
import numpy as np

# Provided data
nparts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
one_dpart = [8.6, 11.96, 13.6, 14.48, 14.79, 17.62, 17.66, 18.06, 20.6, 23.00]
mm_part = [8.7, 11.25, 16.45, 26.97, 48.00, 90.32, 173.14, 342.81, 683.04, 1383.37]
write = [.58, .55, .34, .73, .27, 2.2, .33, .41, .71, 2.86]

# Retry plotting the data

fig, ax = plt.subplots(figsize=(10, 7))

# Plot data
ax.plot(nparts, one_dpart, '-o', label='1D Partition', linewidth=2, markersize=8)
ax.plot(nparts, mm_part, '-s', label='MM Partition', linewidth=2, markersize=8)
ax.plot(nparts, write, '-d', label='Write', linewidth=2, markersize=8)

# Set log-log scale
ax.set_xscale('log', base=2)
ax.set_yscale('log', base=2)

# Set ticks and labels
ax.set_xticks(nparts)
ax.set_xticklabels(nparts)
ax.set_yticks([2**i for i in range(-1, 12)])
ax.set_yticklabels([str(2**i) for i in range(-1, 12)])

# Labels, title, legend
ax.set_xlabel('Number of Parts', fontsize=14, weight='bold')
ax.set_ylabel('Time (seconds)', fontsize=14, weight='bold')
ax.set_title('Partitioning, Populating and Writing Time vs. Number of Parts', fontsize=16, weight='bold')
ax.legend(fontsize=12)
ax.grid(True, which="both", ls="--", c='0.7')
ax.tick_params(axis='both', which='major', labelsize=12)

# Display the plot
plt.tight_layout()
plt.show()
