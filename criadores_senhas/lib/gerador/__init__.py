from lib.interface import *
import string
import random

def criar_nova_senha():

    letras_maisculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    caracteres = letras_maisculas + letras_minusculas + numeros + simbolos

def tratar_senha_fraca():
    password = input('Digite sua senha com base nos requisitos: ')
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    # inicializa as variáveis para armazenar os caracteres faltantes
    faltantes = {'maisculas': '', 'minusculas': '', 'simbolos': ''}

    # Verifica se a senha contém letras maiúsculas
    if not any(char.isupper() for char in password):
        faltantes['maisculas'] = random.choice(letras_maiusculas)
    
    if not any(char.islower() for char in password):
        faltantes['minusculas'] = random.choice(letras_minusculas)

    if not any(char.isdigit() for char in password):
        faltantes['numeros'] = random.choice(numeros)

    if not any(char in '@#$%¨&*' () for char in password):
        faltantes['simbolos'] = random.choice(simbolos)
    
    # Combinar a senha antiga com os caracteres faltantes
    nova_senha = password + ''.join(faltantes.values())

    # Verifica se a senha tem menos de 15 caracteres
    if len(nova_senha) < 15:
        caracteres_faltantes = 15 - len(nova_senha)

        for _ in range(caracteres_faltantes):
            nova_senha += random.choice(string.ascii_latters + string.digits + '@#$%¨&*')
    
    # inserir interface para mostrar nova senha
    # 0---------------------------------------
    # inserir interface para mostrar nova senha
 
def verificar_senha_segura():
    password = input('Digite sua senha com base nos requisitos: ')

    letras_maisculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

     # Verifica se a senha de contém pelo menos uma letra maiúscula
    if not any(char in letras_maisculas for char in password):
        print('A senha não contém letra maiúscula.')
        return
    # Verifica se a senha de contém pelo menos uma letra minusculas
    if not any(char in letras_minusculas for char in password):
        print('A senha não contém letra maiúscula.')
        return
    # Verifica se a senha de contém pelo menos um numero
    if not any(char in numeros for char in password):
        print('A senha não contém letra maiúscula.')
        return
    # Verifica se a senha de contém pelo menos uma letra simbolos
    if not any(char in simbolos for char in password):
        print('A senha não contém letra maiúscula.')
        return
    
    # em teoria o menu 

    # escolha = input(Color.BOLD +"Digite o número da opção desejada: " + Color.END)


    #     if escolha == "1":
    #         criar_nova_senha()
    #     elif escolha == "2":
    #         tratar_senha_fraca()
    #     elif escolha == "3":
    #         verifica_senha_segura()
    #     elif escolha == "0":
    #         print("Saindo...")
    #         break
    #     else:
    #         print("Opção inválida. Por favor, escolha uma das opções listadas.")

# if __name__ = "__main__":
#     menu()
# 1