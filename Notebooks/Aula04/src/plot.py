#!/usr/bin/env python

""" 
%load_ext autoreload
%autoreload 2

from src.plot import plt_data
plt_data([3,4,5], [8,6,3])
"""

# Imports
from matplotlib import pyplot as plt 
import seaborn as sns


# Configs
sns.set_style("darkgrid")
CMAP_VIRIDIS = 'viridis'
PLOT_WIDE = (14,7)

# Funcitons
def plot_heatmap(matrix_correlation, title:str):
    plt.figure(figsize=PLOT_WIDE)
    sns.heatmap(matrix_correlation, fmt='.2f', cmap=CMAP_VIRIDIS, annot=True)
    plt.title(title)
    plt.show()