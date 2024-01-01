#!/usr/bin/env python

from matplotlib import pyplot as plt 
import seaborn as sns
import math

from sklearn.metrics import confusion_matrix

def plt_matrix_confusion(y_test, y_pred, filename, title):
    matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(matrix, annot=True, fmt='.2f', cmap='viridis')
    plt.title(title)
    plt.savefig(filename);
    plt.close();
