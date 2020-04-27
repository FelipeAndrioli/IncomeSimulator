## README

Este eh um pequeno projeto de simulacao de rendimento em um investimento.

Para executar, acesse a pasta de destino atraves de seu terminal e
siga as seguintes instrucoes:

## SEM DOCKER

Para executar sem usar o Docker, basta instalar manualmente a biblioteca 
matplotlib utilizando o comando ```$ pip install matplotlib ```, em seguida
executando com o comando ```$ python main.py```.

## COM DOCKER

Para executar usando Docker, dois comandos serao necessarios:

```
$ docker build -t income-container .

$ docker run -it --rm --name running income-container income-container
```

Logo apos o programa sera executado.


## Observacao

Utilizando a versao sem o Docker a feature do grafico funciona normalmente, entretanto instalando as depedencias com o Docker a feature do grafico nao executa, muito provavelmente por minha falta de conhecimento com as configuracoes do Docker, tentarei resolver nas proximas horas e atualizarei o README

## Observacoes II

Apos muitas pesquisas e testes descobri que Docker nao eh recomenedado para aplicacoes
com interfaces graficas, devido a essa conclusso alterarei parte do escopo do projeto
que consistia em mostrar um grafico de rendimentos para que nao afete o total 
funcionamento do mesmo. 
