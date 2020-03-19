#!/usr/bin/env python3

import matplotlib.pyplot as plt

'''
    Para utilizar o Docker utilizei a biblioteca matplotlib para plotar um grafico
    simples dos investimentos
'''

def initialInstructions():

    '''
        Funcao para inicializacao da aplicacao, eh chamada toda vez que o
        usuario digitar uma opcao invalida ou quando um procedimento for 
        concluido para que as instrucoes possam aparecer novamente.
    '''

    print('\n\t========================================================')
    print('\n\t\t\tSimulador de investimentos\t\t\n')
    print('\t========================================================\n')
    print('\n1 - Investimento do Joao')
    print('\n2 - Faca seu propria simulacao de investimento')
    print('\n3 - Sair do simulador\n')

def investmentJoao():

    '''
        Funcao para o caso do investimento especifico do Joao como o teste 
        tecnico solicitava. 

        weeks - representa  o periodo de investimento em semanas

        investiment - representa a quantidade que Joao investira toda semana

        selic - representa a taxa selic para calculo da rentabilidade

        period - representa o periodo de investimento, como o ano possui 252 dias 
        uteis, os mesmos foram divididos por 12 meses e em seguida por 4 semanas, 
        para que assim houvesse a possibilidade de calculo semanal

        economy - representa a quantia economizada por Joao durante todo o periodo 
        de investimento

        totalInvested - representa a quantia total adquirida por Joao ao final do 
        investimento

        income - representa a quantia que o dinheiro de Joao rendeu no tempo que 
        ele investiu

        totalInvestedPlot - Armazena os valores semanais para serem plotados no 
        grafico

        Formula usada para calculo da rentabilidade: M = P * (1 + i) ^ t / 252

        Essa funcao retorna um relatorio de investimento de Joao chamada 
        investmentReport
    '''

    weeks = 36
    investment = 100.00
    selic = 0.425
    period = (252 / 12) / 4
    economy = 0
    totalInvested = 0
    income = 0
    totalInvestedPlot = []

    for _ in range(weeks):
        economy += investment
        totalInvested = (investment + totalInvested) * (1 + selic) ** (period / 252)
        totalInvestedPlot.append(totalInvested)

    income = totalInvested - economy

    return investmentReport(weeks, investment, economy, income, totalInvested, totalInvestedPlot)

def customInvestment():
    
    '''
        Funcao para o caso de um investimento customizado onde o usuario fornecera
        a quantidade de semanas que deseja investir e o valor a ser investido 
        semanalmente.

        Tem como base a funcao de investimento especifica do Joao
    '''

    while(True):
        try:
            weeks = int(input('Tempo de investimento em semanas: '))
            if(weeks <= 0):
                raise ValueError
            break
        except ValueError:
            print('Forneca um valor valido!')

    while(True):
        try:
            investment = int(input('Valor de investimento por semana: '))
            if(investment <= 0):
                raise ValueError
            break
        except ValueError:
            print('Forneca um valor valido!')

    selic = 0.425
    period = (252 / 12) / 4
    economy = 0
    totalInvested = 0
    totalInvestedPlot = []

    for _ in range(weeks):
        economy += investment
        totalInvested = (investment + totalInvested) * (1 + selic) ** (period / 252)
        totalInvestedPlot.append(totalInvested)

    income = totalInvested - economy

    return investmentReport(weeks, investment, economy, income, totalInvested, totalInvestedPlot)

def investmentOption(option):

    '''
        Funcao para direcionar o usuario para a funcao de investimento desejada,
        caso a opcao selecionada seja 1, o usuario sera direcionado para a funcao
        de investimento especifica de Joao. Caso a opcao seja 2, ele sera direcionado
        para a funcao de investimento customizado, onde ele podera realizar seus
        proprios calculos.
    '''

    if(option == 1):
        return investmentJoao()
    elif(option == 2):
        return customInvestment()

def investmentReport(weeks, investment, economy, income, totalInvested, totalInvestedPlot):

    '''
        Funcao de relatorio de investimentos. Essa funcao retorna um relatorio 
        de investimentos informando o tempo investido em semanas, o valor investido
        em semanas, o valor que foi poupado no tempo de investimento, o valor que 
        o dinheiro investido rendeu no tempo de investimento e o valor final apos
        o periodo de investimento.
    '''

    print('Tempo de investimento: ' + str(weeks) + ' semanas.')
    print('Valor investido por semana R$' + str(round(investment, 2)))
    print('Valor poupado no tempo de investimento R$' + str(round(economy, 2)))
    print('Valor rendido no tempo de investimento R$' + str(round(income, 2)))
    print('Valor total apos o tempo de investimento R$' + str(round(totalInvested, 2)))
    
    while(True):
        try:
            print('1 - Ver o grafico de investimento')
            print('2 - Sair sem ver grafico')
            graphOption = int(input('Selecione sua opcao: '))
            if(graphOption == 1):
                plt.plot(totalInvestedPlot)
                plt.ylabel('Rendimento do valor investido')
                plt.xlabel('Semanas de investimento')
                plt.show()
                break
            elif(graphOption == 2):
                break
            else:
                raise ValueError
        except ValueError:
            print('Digite uma opcao valida!')

def plotInvestimentGraph(weeklyValues):
    plt.plot(weeklyValues)
    plt.ylabel('Total Investido')
    plt.xlabel('Semanas do investimento')
    plt.show()

def main():
    
    '''
        Funcao principal onde verifica a opcao dada pelo usuario e chama a funcao
        que ira direcionar o usuario para o caminho desejado.
    '''

    while(True):
        try:
            initialInstructions()
            option = int(input('Entre com a sua opcao: '))
            if(option < 1 or option > 3):
                raise ValueError
            elif(option == 3):
                break
            else:
                investmentOption(option)
        except ValueError:
            print('Forneca um valor valido!')

if __name__ == "__main__":
    main()
