from lib.interface import *
from lib.gerador import *
from time import sleep

while True:
    resp = menu (['Gerar nova senha', 'Tratar senha fraca', 'Verificar senha segura', 'Sair'])

    if resp == 1:
        criar_nova_senha()
    if resp == 2:
        tratar_senha_fraca()
    if resp == 3:
        verificar_senha_segura()
    if resp == 0:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    
    else:
        cabecalho('ERRO! Digite uma opção válida!')
        sleep(2)