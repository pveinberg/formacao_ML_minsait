Exercício CNN
=============

## Classificação CNN
1. Aquisição e pré-processamento dos dados
2. Treinamento
    1. Implementar arquitetura
    1. Definir otimizadores, métricas e regularizadores
3. Teste (avaliação de desempenho)

Foram implementados 2 scripts:
1. [Implementação CNN básica](./classificacao/script_classificaocao_cnn_local_base.ipynb)
2. [Implementação CNN utilizando Dropout](./classificacao/script_classificaocao_cnn_local_dropout.ipynb)


## Detecção CNN
1. Usar a lib super_gradients(https://github.com/Deci-AI/super-gradients)
2. Utilizar Yolox_nano,PP-YOLOE small ou SSD lite MobileNet v2
   1. Para checar hiper parâmetros disponíveis:
      1. https://github.com/Deci-AI/super-gradients/tree/master/src/super_gradients/recipes
   2. Para checar modelos disponíveis
      1. https://docs.deci.ai/super-gradients/latest/documentation/source/model_zoo.html#computer-vision-models-pretrained-checkpoints
3. Visualizar resultados

## Segmentação CNN
   1. Usar lib segmentation_models(https://github.com/qubvel/segmentation_models)
   2. Usar mobilenet, mobilenetv2 ou seresnet18 como backbone
   3. Usar FPN como arquitetura base
   4. Visualizar resultados

Foram implementados 4 scripts, 1 para cada backbone

1. [mobilenetv2](./segmentacao/segmentacao_mobilenetv2.ipynb)
2. [mobilenet](./segmentacao/segmentacao_mobilenet.ipynb)
3. [resnet18](./segmentacao/segmentacao_resnet18.ipynb)
4. [seresnet18](./segmentacao/segmentacao_seresnet18.ipynb)

### Resumo de desempenho

| BACKBONE    | SCRIPT                        | EPOCHs | TIME FIT | LOSS  | MEAN IOU_SCORE | MEAN F1-SCORE |
|-------------|-------------------------------|--------|----------|-------|----------------|---------------|
| mobilenetv2 | segmentacao_mobilenetv2.ipynb | 10     | 5min 15s | 7,78% | 94,27%         | 97,01%        |
| mobilenet   | segmentacao_mobilenet.ipynb   | 10     | 8min 22s | 7,78% | 95,83%         | 97,83%        |
| resnet18    | segmentacao_resnet18.ipynb    | 10     | 5min 42s | 8,86% | 93,83%         | 96,72%        |
| seresnet18  | segmentacao_seresnet18.ipynb  | 10     | 5min 45s | 8,86% | 93,24%         | 96,39%        |