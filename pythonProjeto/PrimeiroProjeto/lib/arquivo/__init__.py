from lib.interface import *

# Função utilizada para verificar arquivo
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

# Função utilizada para criar o arquivo
def  criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação de arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
# Função utilizada para ler o arquivo
# Função utilizada para ler o arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        cabecalho('PERFUMES CADASTRADOS')
        for linha in a:
            dado = linha.strip().split(';')  # Remove espaços e quebras de linha
            if len(dado) == 2:  # Verifica se a linha contém exatamente 2 elementos
                produto, quantidade = dado
                print(f'{produto:<30}{quantidade:>3} QNTD')
            else:
                print('Linha inválida encontrada no arquivo.')
    finally:
        a.close()

# Função utilizada para fazer o cadastro do objeto
def cadastrar(arq, produto = 'desconhecido', quantidade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    
    else:
        try:
            a.write(f'{produto};{quantidade}\n')

        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Produto adicionado no sitema: {produto}')
            a.close()
