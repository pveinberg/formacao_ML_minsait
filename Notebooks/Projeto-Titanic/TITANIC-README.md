PROJETO TITANIC
===============

## Introdução

Implementar, sobre a base do Titanic - Kaggle -, várias técnicas de ML e gerenciar todas elas com MLFlow


## Passos

1. baixar a base completa
2. preprocessar a base
   1. limpar missing values
   2. validar/limpar duplicados
3. implementar EDAs e mostrar alguns resultados
4. realizar encode dos dados categóricos para numéricos
   1. normalizar dados
   2. dividir features e classe
   3. salvar (pickle) conjuntos de treinamento e teste
5. implementar a base do MLflow para tratar todos os resultados  
6. aplicar as diversas técnicas e colocar no MLflow
   1. naive bayes
   2. árvores decisão
   3. random forest
   4. baseada em instâncias (knn)
   5. regressão logística
   6. redes neurais 
   8. ...
7.  manter o fluxo rodando

## Links

* https://www.kaggle.com/datasets/brendan45774/test-file testes com 418 registros
* https://www.kaggle.com/competitions/titanic/data?select=gender_submission.csv gender submission full

## Dataset Description

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