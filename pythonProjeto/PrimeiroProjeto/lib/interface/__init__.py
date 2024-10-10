# Função utilizada para certificar que o usuário digitou uma opção válida
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número interio válido.')
            continue

        except (KeyboardInterrupt):
            print('O usuário preferiu não inserir os dados')
            return 0
        
        else:
            return n
        
        
# função utilizada para linha
def linha(tam = 42):
    return '-' * tam


# Função utilizada para o cabeçalho
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


# Função utilizada para o Menu
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1

    for i in lista:
        print(f'{c} - {i}')
        c += 1

    print(linha()) 

    opc = leiaInt('Sua Opção: ')
    return opc
