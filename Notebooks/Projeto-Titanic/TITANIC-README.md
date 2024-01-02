PROJETO MLflow - TITANIC
========================

## Introdução

Implementar, sobre O [dataset de sobreviventes do Titanic](https://www.kaggle.com/competitions/titanic/data?select=gender_submission.csv) no Kaggle, várias técnicas de ML e gerenciar todas elas usando [MLFlow](https://mlflow.org/docs/latest/index.html)

## Passos

1. Baixar o dataset (./datasets/raw/train.csv);
2. Preprocessar o conjunto de dados:
   1. Limpar missing values;
   2. Validar/limpar duplicados;
   3. Persistir dataset processado.
3. implementar EDAs e mostrar alguns resultados;
4. Realizar `encode` dos dados categóricos para numéricos:
   1. Realizar `encode`;
   2. Normalizar dados;
   3. Dividir features e classe (X, y)
   4. Dividir datasets de treinamento e teste;
   5. Salvar (usando `pickle`) os conjuntos de treinamento e teste.
5. Implementar base de MLflow para tratar todos os resultados.  
6. Aplicar técnicas de ML e volcar resultados no MLflow:
   1. Naive Bayes
   2. Árvores Decisão
   3. Random Forest
   4. KNN - Baseada Em Instâncias
   5. Regressão Logística
   6. Redes Neurais (Pendente)

## Dataset Description
[from Kaggle]

### Overview
The data has been split into two groups:

* training set (train.csv)
* test set (test.csv)

The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use feature engineering to create new features.

The test set should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

We also include gender_submission.csv, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

### Data Dictionary

Variable|Definition|Key
--------|----------|---
survival|Survival|0 = No, 1 = Yes
pclass|Ticket class|1 = 1st, 2 = 2nd, 3 = 3rd
sex|Sex|
Age|Age in years|
sibsp|# of siblings / spouses aboard the Titanic|
parch|# of parents / children aboard the Titanic|
ticket|Ticket number|
fare|Passenger fare|
cabin|Cabin number|
embarked|Port of Embarkation|C = Cherbourg, Q = Queenstown, S = Southampton

### Variable Notes
**pclass:** A proxy for socio-economic status (SES)
* 1st = Upper
* 2nd = Middle
* 3rd = Lower

**age:** Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

**sibsp:** The dataset defines family relations in this way...

* Sibling = brother, sister, stepbrother, stepsister
* Spouse = husband, wife (mistresses and fiancés were ignored)

**parch:** The dataset defines family relations in this way...
* Parent = mother, father
* Child = daughter, son, stepdaughter, stepson

Some children travelled only with a nanny, therefore parch=0 for them.