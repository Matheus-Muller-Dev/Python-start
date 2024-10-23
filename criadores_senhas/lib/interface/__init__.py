import os
import platform
from colorama import init, Fore

class Color:
    RED = '\033[91m'  # Vermelho
    GREEN = '\033[92m'  # Verde
    # caso desejar usar mais cores
    # YELLOW = '\033[93m'  # Amarelo
    # BLUE = '\033[94m'  # Azul
    # MAGENTA = '\033[95m'  # Magenta
    # CYAN = '\033[96m'  # Ciano
    # WHITE = '\033[97m'  # Branco

    # Formatação de texto
    # BOLD = '\033[1m'  # Negrito
    # UNDERLINE = '\033[4m'  # Sublinhado
    # END = '\033[0m'  # Resetar formatação
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
    print(Color.GREEN + linha())
    print(Color.GREEN + txt.center(42))
    print(Color.GREEN + linha())

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