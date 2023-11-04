Exercício CNN
=============

## Classificação CNN
1. Aquisição e pré-processamento dos dados
2. Treinamento
    1. Implementar arquitetura
    1. Definir otimizadores, métricas e regularizadores
3. Teste (avaliação de desempenho)

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



| BACKBONE    | SCRIPT                        | EPOCHs | TIME FIT | LOSS   | MEAN IOU_SCORE | MEAN F1-SCORE |
|-------------|-------------------------------|--------|----------|--------|----------------|---------------|
| mobilenetv2 | segmentacao_mobilenetv2.ipynb | 10     | 5min 15s | 12,20% | 95,95%         | 97,90%        |
| mobilenet   | segmentacao_mobilenet.ipynb   | 10     | 5min 10s | 11,95% | 95,81%         | 97,83%        |
| resnet18    | segmentacao_resnet18.ipynb    | 10     | 4min 10s | 11,64% | 93,13%         | 96,37%        |
| seresnet18  | segmentacao_seresnet18.ipynb  | 10     | 4min 30s | 12,97% | 92,39%         | 95,94%        |