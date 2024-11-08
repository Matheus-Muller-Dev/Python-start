import os
import platform
#
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO!  Pro favor digite um número inteiro válido.')
            continue

        except (KeyboardInterrupt):
            print('O usuário preferiu não inserir os dados')
            return 0
        
        else:
            return n

# aqui podemos definir as arestas de parte superior e inferior
def linha(tam = 42):    
    return '=' * tam

#
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#
def menu(lista):
    cabecalho('GERADOR DE SENHA')
    c = 1

    for i in lista:
        print(f'{c} - {i}')
        c += 1

    print(linha())

    opc = leiaInt('Sua Opção: ')
    return opc

def infolista(texto):
    print(linha())

    for i in texto:
        print(f'{i}')

    print(linha())

def limpar_tela():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')