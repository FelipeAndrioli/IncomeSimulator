#!/usr/bin/env python3

def initialInstructions():
    print('\n\t========================================================')
    print('\n\t\t\tSimulador de investimentos\t\t\n')
    print('\t========================================================\n')
    print('\n1 - Investimento do Joao')
    print('\n2 - Faca seu propria simulacao de investimento')
    print('\n3 - Sair do simulador\n')

def investmentJoao():
    weeks = 36
    investment = 100.00
    selic = 0.425
    period = (252 / 12) / 4
    economy = 0
    totalInvested = 0
    
    for _ in range(weeks):
        economy += investment
        totalInvested = (investment + totalInvested) * (1 + selic) ** (period / 252)
    
    income = totalInvested - economy

    return investmentReport(weeks, investment, economy, income, totalInvested)

def customInvestment():
    
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

    for _ in range(weeks):
        economy += investment
        totalInvested = (investment + totalInvested) * (1 + selic) ** (period / 252)

    income = totalInvested - economy

    return investmentReport(weeks, investment, economy, income, totalInvested)

def investmentOption(option):
    if(option == 1):
        return investmentJoao()
    elif(option == 2):
        return customInvestment()

def investmentReport(weeks, investment, economy, income, totalInvested):

    print('Tempo de investimento: ' + str(weeks) + ' semanas.')
    print('Valor investido por semana R$' + str(round(investment, 2)))
    print('Valor poupado no tempo de investimento R$' + str(round(economy, 2)))
    print('Valor rendido no tempo de investimento R$' + str(round(income, 2)))
    print('Valor total apos o tempo de investimento R$' + str(round(totalInvested, 2)))

def main():
    
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
