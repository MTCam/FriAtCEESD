import sys
import argparse
import matplotlib.pyplot as plt
from typing import List, Tuple


def get_coverage_data(file):

    # Read coverage data from file
    with open(file, "r") as f:
        data = f.readlines()
    
    # Parse data and store in dict
    coverage = {}
    for line in data:
        file, lines, covered, percent = line.split()
        file = file.replace("mirgecom/", "")  # remove "mirgecom/" from line
        percent = int(percent[:-1])  # remove % sign and convert to int
        coverage[file] = percent
    
    # Sort files by coverage category
    excellent = []
    good = []
    fair = []
    poor = []
    for file, percent in coverage.items():
        if percent >= 90:
            excellent.append((file, percent))
        elif percent >= 80:
            good.append((file, percent))
        elif percent >= 60:
            fair.append((file, percent))
        else:
            poor.append((file, percent))
    
    # Sort files within each category alphabetically
    excellent = sorted(excellent, key=lambda x: x[0])
    good = sorted(good, key=lambda x: x[0])
    fair = sorted(fair, key=lambda x: x[0])
    poor = sorted(poor, key=lambda x: x[0])
    
    # Combine files in order of coverage category
    files = []
    files.extend(excellent)
    files.extend(good)
    files.extend(fair)
    files.extend(poor)
    
    return files


def plot_coverage(data):
    labels = []
    coverage = []
    colors = []
    for file, percent in data:
        labels.append(file)
        coverage.append(percent)
        if percent >= 90:
            colors.append('green')
        elif percent >= 80:
            colors.append('limegreen')
        elif percent >= 60:
            colors.append('gold')
        else:
            colors.append('red')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, coverage, color=colors)
    ax.set_xticklabels(labels, rotation=90)
    fig.subplots_adjust(bottom=0.40)
    ax.set_xlabel("File", fontdict={'fontsize': 14})
    ax.set_ylabel("Coverage (%)", fontdict={'fontsize': 14})
    ax.set_title(r"$\it{MIRGE-Com}$ Testing Coverage (main)", fontdict={'fontsize': 16})
    plt.show()
    return fig, ax

if __name__ == '__main__':
    data = get_coverage_data("coverage_report_main.txt")
    fig, ax = plot_coverage(data)
    fig.savefig("coverage_plot_main.pdf")

