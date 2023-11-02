# Reloading the data
data = {
    'mesh_size': [24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576],
    'gmsh_read': [0.56, 1.07, 2.07, 3.94, 7.45, 14.57, 27.60, 53.63, 105.52, 205.53, 399.86],
    'data_pop': [1.02, 2.02, 4.00, 7.63, 14.61, 27.14, 50.63, 97.05, 188.58, 366.89, 746.89],
    'mem': [0.859, 0.910, 1.004, 1.193, 1.557, 2.251, 3.388, 5.869, 10.784, 20.487, 39.380]
}

# Adjusting y-axis limits
fig, ax1 = plt.subplots(figsize=(10, 7))

# Plotting the gmsh_read and data_pop times
ax1.set_xlabel('Mesh Size (in thousands of elements)', fontsize=14, weight='bold')
ax1.set_ylabel('Time (seconds)', fontsize=14, weight='bold')
ax1.set_yscale('log', basey=2)
ax1.set_ylim(2**-1, 2**10)  # Adjusting y-axis limits

ln1 = ax1.plot(data['mesh_size'], data['gmsh_read'], 'o-', label='gmsh_read', linewidth=2, markersize=8)
ln2 = ax1.plot(data['mesh_size'], data['data_pop'], 's-', label='data_pop', linewidth=2, markersize=8)

# Creating the second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Memory (GB)', fontsize=14, weight='bold')
ax2.set_yscale('log', basey=2)
ax2.set_ylim(2**-1, 2**10)  # Adjusting y-axis limits to log2(1000)
ln3 = ax2.plot(data['mesh_size'], data['mem'], 'd-', label='Memory', color='purple', linewidth=2, markersize=8)

# Styling and displaying the plot
lns = ln1 + ln2 + ln3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=2)

ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_title("Mesh Processing Times and Memory Usage", fontsize=16, weight='bold')
plt.xscale("log", base=2)
plt.xticks(data['mesh_size'], labels=data['mesh_size'], rotation=45)

plt.tight_layout()
plt.show()
