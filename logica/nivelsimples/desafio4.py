# A função inserida para verificar idade.
def verificar_idade(idade):
    # condicional para o processamento de idade.
    if (idade >= 18):
        print("Você é maior de idade. ")
    else:
        print("Você é menor de idade. ")
    return idade

# a entrada de dados
idade = int(input("Qual é a sua idade: "))

# a saida de dados
verificar_idade(idade)

