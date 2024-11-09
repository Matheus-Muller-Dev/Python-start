def calcular_raiz_aproximada(numero, margem_erro):
    aproximacao = numero
    while abs(aproximacao * aproximacao - numero) > margem_erro:
        aproximacao = (aproximacao + numero / aproximacao) / 2
    return aproximacao

numero = 25 
margem_erro = 0.0001
raiz_aproximada = calcular_raiz_aproximada(numero, margem_erro)
print(raiz_aproximada)