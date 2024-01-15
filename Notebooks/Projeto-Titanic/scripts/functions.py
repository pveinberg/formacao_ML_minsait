#!/usr/bin/env python

from matplotlib import pyplot as plt 
import seaborn as sns
import math

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

# returns a dict with accuracy, precision, recall, f1_score, support (avg for last 4 metrics)
def get_metrics(y_test, y_pred, filename, title):
    matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(matrix, annot=True, fmt='.2f', cmap='viridis')
    plt.title(title)
    plt.savefig(filename);
    plt.close();

    class_report = classification_report(y_test, y_pred, 
                           output_dict=True)

    results = class_report['macro avg']
    results['accuracy'] = accuracy_score(y_test, y_pred)
    return results        

def get_best_model(estimator_, all_params_, X_train_, y_train_):
    grid = GridSearchCV(estimator=estimator_, \
                        param_grid=all_params_, \
                        refit=True)
    
    grid.fit(X_train_, y_train_)
    return grid