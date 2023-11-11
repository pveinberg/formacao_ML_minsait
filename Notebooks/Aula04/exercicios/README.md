PRÁTICA MLFLOW
==============

1. Treine um classificador de ensemble e uma rede do keras para o dataset de diabetes.
[Script](https://github.com/pveinberg/formacao_ML_minsait/blob/7b08f3b33c17f9559efd877ee7196aa760de0e58/Notebooks/Aula04/exercicios/exercicio_mlflow_ensamble_keras_diabetes.ipynb)

2. Treine um classificador com CNN para o dataset de imagens do cérebro
[PENDENTE]

3. Nomeie seu experimento Grupo seguido de underscore, seguido dos primeiros nomes de cada participante do grupo separados por underscore exemplo: "Grupo_Diego_Thais" 
`Exercicio_Keras_Grupo_Ivandro_Pablo`

4. Use MLFLow para salvar as ***estatísticas*** e ***hiperparametros*** de cada modelo.
[fazer prints de tela após implementação do CNN]

5. Faça deploy ***localmente*** de cada modelo

**Random Forest**
`mlflow models serve -m runs:/bd93f474eeae429fb5c242fcb4c18ca4/"Random_Forest --port=5001 --env-manager local`

**Keras**
`mlflow models serve -m runs:/81e519aaa7684252ad1be41752efa72b/Keras_Model --port=5002 --env-manager local`

6. Faça uma requisição pro deploy de cadas modelo

[Script requisição keras](https://github.com/pveinberg/formacao_ML_minsait/blob/7b08f3b33c17f9559efd877ee7196aa760de0e58/Notebooks/Aula04/exercicios/requisicao-keras.ipynb)

[Script requisição random forest](https://github.com/pveinberg/formacao_ML_minsait/blob/7b08f3b33c17f9559efd877ee7196aa760de0e58/Notebooks/Aula04/exercicios/requisicao-random-forest.ipynb)

- Inclua no envio: 
  - Os ***arquivos*** do modelo
  - Um ***print*** da ***ui*** do mlflow com ***estatisticas*** e ***hiperparametros*** do seu modelo
  - Requisição feita para o modelo
  - Resposta da requisição feita para o modelo