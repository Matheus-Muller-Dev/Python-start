from lib.interface import *
import string
import random

def criar_nova_senha():
    cabecalho('Uma senha segura deve conter: ')
    infolista(['-- Letra maiúscula', '-- Letra maiúscula', '-- Números', '-- Símbolos @#$%¨&*'])

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    senha = ''.join(random.sample(caracteres, 15))

    limpar_tela()
    cabecalho(f'Nova Senha: {senha}')

def tratar_senha_fraca():
    limpar_tela()
    cabecalho('Melhorar senha: ')
    infolista(['-- Você deve colocar sua senha existente: ', '-- iremos retornar uma senha mais forte'])

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

    if not any(char in '@#$%¨&*' for char in password):
        faltantes['simbolos'] = random.choice(simbolos)
    
    # Combinar a senha antiga com os caracteres faltantes
    nova_senha = password + ''.join(faltantes.values())

    # Verifica se a senha tem menos de 15 caracteres
    if len(nova_senha) < 15:
        caracteres_faltantes = 15 - len(nova_senha)

        for _ in range(caracteres_faltantes):
            nova_senha += random.choice(string.ascii_letters + string.digits + '@#$%¨&*')

    limpar_tela()
    cabecalho(f'Senha tratada com sucesso, nova senha: {nova_senha}')
 
def verificar_senha_segura():
    limpar_tela()
    cabecalho('VERIFICAR SENHA SEGURA:')
    infolista(['--Vamos verificamos se a senha é segura ou não', '- Você deve colocar sua senha existente:'])

    password = input('Digite sua senha com base nos requisitos: ')
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    limpar_tela()
     # Verifica se a senha de contém pelo menos uma letra maiúscula
    if not any(char in letras_maiusculas for char in password):
        cabecalho('A senha não contém letra maiúscula.')
        return
        
    
    # Verifica se a senha de contém pelo menos uma letra minusculas
    if not any(char in letras_minusculas for char in password):
        cabecalho('A senha não contém letra minusculas.')
        return
    
    # Verifica se a senha de contém pelo menos um numero
    if not any(char in numeros for char in password):
        cabecalho('A senha não contém números.')
        return
    
    # Verifica se a senha de contém pelo menos uma letra simbolos
    if not any(char in simbolos for char in password):
        cabecalho('A senha não contém simbolos.')
        return
    
    cabecalho('SENHA SEGURA!')