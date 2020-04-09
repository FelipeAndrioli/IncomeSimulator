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


## Observação

Utilizando a versão sem o Docker a feature do gráfico funciona normalmente, entretanto instalando as depedências com o Docker a feature do gráfico não executa, muito provavelmente por minha falta de conhecimento com as configurações do Docker, tentarei resolver nas próximas horas e atualizarei o README

## Observa��o II

Ap�s muitas pesquisas e testes descobri que Docker n�o érecomenedado para aplica��es
com interfaces gr�ficas, devido a essa conclus�o alterarei parte do escopo do projeto
que consistia em mostrar um gr�fico de rendimentos para que n�o afete o total 
funcionamento do mesmo. 
