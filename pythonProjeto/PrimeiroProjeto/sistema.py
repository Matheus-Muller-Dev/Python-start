# importando as bibliotecas
from lib.interface import *
from lib.arquivo import *
from time import sleep

# Variável para armazenar o arquivo txt
arq = 'banco.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

# -------------------------------------------------
def apagarUsuario(arquivo, perfume):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()  # Corrigido para ler todas as linhas
        
        with open(arquivo, 'w') as file:
            perfume_removido = False
            for linha in linhas:
                if perfume not in linha:  # Se o nome não está na linha, reescreva a linha
                    file.write(linha)
                else:
                    perfume_removido = True
                    
        if perfume_removido:
            print(f'Produto {perfume} foi removido com sucesso! ')
        else:
            print(f'Produto {perfume} não foi encontrado.')
    except FileNotFoundError:
        print('Arquivo não foi encontrado.')
# -------------------------------------------------
def editarProduto(arquivo, perfume, nova_quantidade):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()  # Lê todas as linhas do arquivo
            
        with open(arquivo, 'w') as file:
            produto_editado = False
            for linha in linhas:
                # Verifica se a linha tem o formato esperado
                if ';' in linha:  # Verifica se a linha contém o separador esperado
                    nome, quantidade = linha.strip().split(';')  # Assume que o formato é "Nome - Quantidade"
                    if nome == perfume:
                        nova_linha = f'{nome};{nova_quantidade}\n'   # Atualiza a linha com a nova quantidade
                        file.write(nova_linha)
                        produto_editado = True
                        print(f"Produto {nome} editado com sucesso! Nova quantidade: {nova_quantidade}")
                    else:
                        file.write(linha)  # Reescreve a linha sem alterações se o nome não coincide
                else:
                    file.write(linha)  # Reescreve a linha se não tiver o formato esperado

        if not produto_editado:
            print(f'Produto {perfume} não foi encontrado para editar.')
    except FileNotFoundError:
        print('Arquivo não foi encontrado.')


# Estrutura de repetição para rodar o programa até o usuário dar a opção: "Sair do programa"
while True:
    resp = menu(['Ver Produto no Estoque', 'Cadastrar novo Produto', 'Editar Quantidade do Produto', 'Apagar Produto do Estoque', 'Sair do sistema'])

    if resp == 1:
        lerArquivo(arq)

    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        perfume = str(input('Nome do produto: '))
        quantidade = leiaInt('Quantidade: ')
        cadastrar(arq, perfume, quantidade)

    elif resp == 3:
        cabecalho('EDITAR PRODUTO EXISTENTE')
        perfume = str(input('Qual produto gostaria de editar: '))
        nova_quantidade = leiaInt('Nova quantidade: ')
        editarProduto(arq, perfume, nova_quantidade)

    elif resp == 4:
        cabecalho('APAGAR PRODUTO')
        perfume = str(input('Qual produto gostaria de apagar: '))
        apagarUsuario(arq, perfume)

    elif resp == 5:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break

    else:
        cabecalho('ERRO! Digite uma opção válida!')
        sleep(2)
