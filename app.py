#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import anylearn

# Inicializa o SDK com os parâmetros diretamente
anylearn.init_sdk('http://10.101.67.7:30080', 'yhuang', 'Anylearn2021!')

# Executa o treinamento com os parâmetros definidos
task, _, _, _ = anylearn.quick_train(
    algorithm_name="ToyAlgo",
    algorithm_dir=".",
    algorithm_force_update=True,
    entrypoint="python train.py",
    output="results",
    dataset_id="DSETf6c6f7584cfb9b01d69f25bb9bc7",
    dataset_hyperparam_name='datadir',
    model_id="MODE885079a5405185639e8de08f5ffb",
    model_hyperparam_name='modeldir',
    pretrain_task_id="TRAId8be326641f78134edaa51385cae",
    pretrain_hyperparam_name="checkpointdir",
    hyperparams={
        'epochs': 12,
        'model': 'BiT-M-R50x1',
    },
)

# Exibe o objeto da tarefa retornada
print("[INFO] Tarefa iniciada com sucesso:")
print(task)
