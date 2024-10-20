# importações
from lib.interface import *
from lib.operacoes import *
from time import sleep

while True:
    # opções que irá ser visualizada no terminal
    resp = menu(['Soma', 'Multiplicação', 'Subtração', 'Divisão', 
                 'Raiz Quadrada', 'Quadrado de um Número', 'Sair'])
	# Caso seja selecionado a opção 1
    if resp == 1:
        cabecalho('SOMA')
        a = input('Qual é o primeiro número: ')
        b = input('Qual é o segundo número: ')
        print(f'Resultado: {somar(a, b)}')
	# Caso seja selecionado a opção
    elif resp == 2:
        cabecalho('MULTIPLICAÇÃO')
        a = input('Qual é o primeiro número: ')
        b = input('Qual é o segundo número: ')
        print(f'Resultado: {multiplicar(a, b)}')
	# Caso seja selecionado a opção
    elif resp == 3:
        cabecalho('SUBTRAÇÃO')
        a = input('Qual é o primeiro número: ')
        b = input('Qual é o segundo número: ')
        print(f'Resultado: {subtrair(a, b)}')
	# Caso seja selecionado a opção
    elif resp == 4:
        cabecalho('DIVISÃO')
        a = input('Qual é o numerador: ')
        b = input('Qual é o denominador: ')
        print(f'Resultado: {divisao(a, b)}')
	# Caso seja selecionado a opção
    elif resp == 5:
        cabecalho('RAIZ QUADRADA')
        a = input('Qual número deseja calcular a raiz quadrada: ')
        print(f'Resultado: {raiz_quadrada(a)}')
	# Caso seja selecionado a opção
    elif resp == 6:
        cabecalho('QUADRADO DE UM NÚMERO')
        a = input('Qual número deseja elevar ao quadrado: ')
        print(f'Resultado: {quadrado(a)}')
	# Caso seja selecionado a opção
    elif resp == 7:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida! Tente novamente.')
    
    sleep(1)
