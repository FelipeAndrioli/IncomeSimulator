## README

Este é um pequeno projeto de simulação de rendimento em um investimento.

Para executar, acesse a pasta de destino através de seu terminal e
siga as seguintes instruções:

## SEM DOCKER

Para executar sem usar o Docker, basta instalar manualmente a biblioteca 
matplotlib utilizando o comando ```$ pip install matplotlib ```, em seguida
executando com o comando ```$ python main.py```.

## COM DOCKER

Para executar usando Docker, dois comandos serão necessários:

```
$ docker build -t income-container .

$ docker run -it --rm --name running income-container income-container
```

Logo após o programa sera executado.
