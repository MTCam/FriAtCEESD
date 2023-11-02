# Data
data = {
    'mesh_sizes': [24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576],
    'gmsh_read': [0.56, 1.07, 2.07, 3.94, 7.45, 14.57, 27.60, 53.63, 105.52, 205.53, 399.86],
    'data_pop': [1.02, 2.02, 4.00, 7.63, 14.61, 27.14, 50.63, 97.05, 188.58, 366.89, 746.89],
    'memory': [0.859, 0.910, 1.004, 1.193, 1.557, 2.251, 3.388, 5.869, 10.784, 20.487, 39.380]
}

# Plotting the data again without the xlim error

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting the gmsh_read and data_pop on left y-axis
ax1.set_xlabel('Mesh Size (1000s of Elements)')
ax1.set_ylabel('Time (s)', color='tab:blue')
ax1.set_yscale("log", base=2)
ax1.plot(mesh_sizes, data['gmsh_read'], 'o-', label="gmsh_read", color='tab:blue')
ax1.plot(mesh_sizes, data['data_pop'], 's-', label="data_pop", color='tab:orange')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')

# Making the right y-axis for memory
ax2 = ax1.twinx()
ax2.set_ylabel('Memory (GB)', color='tab:red')
ax2.plot(mesh_sizes, data['mem'], 'd-', color='tab:red', label="Memory")
ax2.set_yscale("log", base=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

# Setting x-axis to log scale
ax1.set_xscale("log", base=2)
ax1.set_xticks(mesh_sizes)
ax1.get_xaxis().set_major_formatter(ScalarFormatter())

# Setting title and grid
plt.title("Time to Process the Mesh and Memory Usage")
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
