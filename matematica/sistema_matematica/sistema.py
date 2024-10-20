from lib.interface import *
from time import sleep

while True:
	resp = menu(['Multiplicação', 'subtração', 'Divisão', 'Raiz quadrada', 'Quadrado de um número'])

	if resp == 1:
	cabecalho('MULTIPLICAÇÃO')
	primeiro_recebido = str(input('Qual primeiro número para multiplicar'))
	segundo_numero = str(input('Qual o segundo número para multiplicar'))
	multiplicar(primeiro_numero, segundo_numero)

	if resp == 2:
	cabecalho('SUBTRAÇÃO')
	primeiro_numero = str(input('Qual segundo número para multiplicar'))
	segundo_numero = str(input('Qual o segundo número para multiplicar'))
	subtracao(primero_numero, segundo_numero)

	if resp == 3:
	cabecalho('DIVISÃO')
	primeiro_numero = str(input('Qual segundo número para multiplicar'))
	segundo_numero = str(input('Qual o segundo número para multiplicar'))
	divisao(primero_numero, segundo_numero)

	if resp == 4:
	cabecalho('RAIZ QUADRADA')
	primeiro_numero = str(input('Qual segundo número para multiplicar'))
	segundo_numero = str(input('Qual o segundo número para multiplicar'))
	raiz_quadrada(primero_numero, segundo_numero)

	if resp == 5:
	cabecalho('QUADRADO DE UM NÚMERO')
	primeiro_numero = str(input('Qual segundo número para multiplicar'))
	segundo_numero = str(input('Qual o segundo número para multiplicar'))
	raiz_quadrada(primero_numero, segundo_numero)

