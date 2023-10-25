# Classificação de tipos de tumores
# =================================
# 
# **Imagens na pasta Datasets/Exercicio_Tumores**
# 
# **Passos:**
# 
# 1. Carregue o conjunto de imagens.
# 2. Realize o pre processamento.
# 3. Divida os dados em recursos (X) e rótulos (y).
# 4. Divida o conjunto de dados em conjuntos de treinamento, validação e teste.
# 5. Treinamento: 
#    1. Definição de arquitetura:
#       1. Definir quantas camadas são necessárias para o problema
#       2. A quantidade de neurônios em cada camada.
#       3. A função de ativação de cada camada.
#       4. Regularização - dropout.
#       5. A função de ativação da saída.
#          * softmax (saída não binária).
#          * sigmoid (saída binária).
#    2. `.compile`: Definição dos otimizadores.
#    3. Regularização - earlystop.
#    4. `.fit`: Adicionar conjuntos de treinamento e validação; e determinar a quantidade de épocas.
# 6. Avalie o desempenho do modelo usando métricas como acurácia, matriz de confusão, etc. 

# ## Imports

import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, confusion_matrix

from keras.layers import Dense, Activation, Dropout, Flatten
from keras.models import Sequential
from keras.callbacks import EarlyStopping

import pathlib
import cv2
import os

import matplotlib.pyplot as plt

import sys 
sys.path.insert(1, '../')
from src.plot import plot_heatmap
from src.train import get_all_subsets, results_regression

# 1. Aquisição dos dados

path = '../../Datasets/Exercicio_Tumores'
data = pathlib.Path(path)

disease = {
    "glioma_tumor": list(data.glob('glioma_tumor/*.jpg')),
    "meningioma_tumor": list(data.glob('meningioma_tumor/*.jpg')),
    "normal": list(data.glob('normal/*.jpg')),
    "pituitary_tumor" : list(data.glob('pituitary_tumor/*.jpg')),       
}

labels = {
    "glioma_tumor" : 0,
    "meningioma_tumor": 1,
    "normal": 2,
    "pituitary_tumor": 3
}

directory = os.listdir(path)

for each in disease.keys():
    plt.figure(figsize=(10, 10))
    currentFolder = path + '/' + each
    for i, file in enumerate(os.listdir(currentFolder)[0:5]):
        fullpath = path + '/' + each + "/" + file
        img=cv2.imread(fullpath)
        ax=plt.subplot(1,5,i+1)
        ax.set_title(file)
        if(i == 0):
            ax.set_ylabel(each)
        else:
            ax.set_yticklabels([])
        plt.imshow(img)

# Carregamento dos dados

X = []
Y = []
for name, diseases in disease.items():
    for disease in diseases:
        img = cv2.imread(str(disease))
        img = img.astype('float32') / 255.0
        X.append(img)
        Y.append(labels[name])     

X = np.array(X)
Y = np.array(Y)

X_train, X_val, X_test, y_train, y_val, y_test = get_all_subsets(X, Y)

print('X_train: ', X_train.shape)
print('X_val: ', X_val.shape)
print('X_test: ', X_test.shape)
print('y_train: ', y_train.shape)
print('y_val: ', y_val.shape)
print('y_test: ', y_test.shape)

hot = OneHotEncoder()
y_train = hot.fit_transform(np.array(y_train).reshape(-1, 1)).toarray()
y_val = hot.fit_transform(np.array(y_val).reshape(-1, 1)).toarray()
y_test = hot.transform(np.array(y_test).reshape(-1, 1)).toarray()

seq = Sequential()
seq.add(Flatten(input_shape = (256, 256, 3)))
seq.add(Dense(512))
seq.add(Activation('relu'))
seq.add(Dropout(0.3))
seq.add(Dense(256))
seq.add(Activation('relu'))
seq.add(Dense(128))
seq.add(Dropout(0.3))
seq.add(Activation('relu'))
seq.add(Dense(64))
seq.add(Activation('relu'))
seq.add(Dense(4))
seq.add(Activation('softmax'))

seq.compile(loss = 'categorical_crossentropy', optimizer = 'Adam', metrics=['accuracy'])

print(seq.summary())

es = EarlyStopping(monitor = 'val_loss', min_delta = 0.001, patience = 10, verbose = 1, mode = 'auto')

historico = seq.fit(X_train, y_train, \
                             epochs = 50, 
                             verbose = 1,
                             validation_data = (X_val, y_val),
                             callbacks = [es])


y_pred = seq.predict(X_test)

print("Accuracy score:\n\r", "=="*20)
print(accuracy_score(y_test.argmax(1), y_pred.argmax(1)))

print("Confusion Matrix:\n\r")
print(confusion_matrix(y_test.argmax(1), y_pred.argmax(1)))