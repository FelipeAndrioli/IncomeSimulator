## README

Este eh um pequeno projeto de simulacao de rendimento em um investimento

Para executar, acesse a pasta de destino atraves de seu terminal e
siga as seguintes instrucoes:

## SEM DOCKER

Para executar sem usar o Docker, basta baixar manualmente a biblioteca 
matplotlib utilizando o comando ```pip install matplotlib ```, em seguida
executando com o comando ```python main.py```.

## COM DOCKER

Para executar usando Docker, dois comandos serao necessarios:

	```docker build -t income-container .```

	```docker run -it --rm --name running income-container income-container```

Logo apos o programa sera executado.
