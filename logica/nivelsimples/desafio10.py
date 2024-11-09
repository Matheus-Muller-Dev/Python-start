# Função para classificar o triângulo
def classificar_triangulo():
    # recebe os valores de entrada
    l1 = float(input("qual tamanho do primeiro lado: "))
    l2 = float(input("qual tamanho do segundo lado: "))
    l3 = float(input("qual tamanho do terceiro lado: "))

    # Verificação de validade do triângulo
    if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
        return "Não é um triângulo válido"

    # Classificação pelo comprimento dos lados
    if l1 == l2 == l3:
        classificacao_lados = "Equilátero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        classificacao_lados = "Isósceles"
    else:
        classificacao_lados = "Escaleno"

    # Classificação pelo ângulo usando o maior lado como base comparação
    lados = sorted([l1, l2, l3])
    if lados[0] ** 2 + lados[1] ** 2 > lados[2] ** 2:
        classificacao_angulos = "Acutângulo"
    elif lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2:
        classificacao_angulos = "Retângulo"
    else:
        classificacao_angulos = "Obtusângulo"

    return f"Triângulo {classificacao_lados} e {classificacao_angulos}"

# Chamando a função
print(classificar_triangulo())