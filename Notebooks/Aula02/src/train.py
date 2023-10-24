#!/usr/bin/env python

""" 
%load_ext autoreload
%autoreload 2

from src.plot import plt_data
plt_data([3,4,5], [8,6,3])
"""

# Imports
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, \
    mean_absolute_percentage_error, r2_score
import numpy as np
import math


# ====================================================================================================
# Functions
# ====================================================================================================


# Função que retorna subconjunto de treino, validação e teste
def get_all_subsets(X, y, test_size=0.2, random_state=42):
    # split train, test
    X_train, X_test, y_train, y_test = train_test_split(X, y, \
                                                        test_size=test_size, random_state=random_state)
    
    # split train, validate
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, \
                                                      test_size=test_size, random_state=random_state)
    
    return X_train, X_val, X_test, y_train, y_val, y_test 

# Função de mostra e retorna métricas de análise para regressão
def results_regression(y_test, y_pred, print_ = False):
    y_pred = y_pred.astype(np.int64)
    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    if print_:
        print(f"MSE: {mse}")
        print(f"Erro médio quadrático (RMSE): {rmse}")    
        print(f"Erro médio absoluto (MAE): {mae}")
        print(f"Erro de porcentagem absoluta média (MAPE): {mape}")
        print(f"R2 Score: {r2}")
        
    return mse, rmse, mae, mape, r2