#De forma simplificada
grausCelsius = 100
fahrenheit = 100

Total_fahrenheit = grausCelsius * 1.8 + 32
Total_Celsius = (fahrenheit - 32) * 1.8

print(f"A conversão de Celsius para fahrenheit é {Total_fahrenheit}°C")
print(f"A conversão de Fahrenheit para Celsius é {Total_Celsius}°C")

# Conversor de unidades: Graus Celsius e Fahrenheit
# Mais completo e com estrutura de condicionais para converter ambos
# def menu_inicial():
#     print('Programa para conversão de Temperaturas')
#     print('1. Converter de Celsius para Fahrenheit')
#     print('2. Converter de Fahrenheit para celsius')
# 
# def cel_fahr():
#     Celsius = float(input('Entre com a temperatura em graus Celsius: '))
#     Fahrenheit = Celsius * 1.8 + 32
#     print("O valor em Fahrenheit: {0}°F".format(Fahrenheit))
# 
# def fahr_cel():
#     Fahrenheit = float(input('Entre com a temperatura em Fahrenheit: '))
#     Celsius = (Fahrenheit - 32) * 1.8
#     print('Valor em Celsius: {0}°C'.format(Celsius))
# 
# if __name__=='__main__':
#     menu_inicial()
#     escolha = input('Escolha o tipo de conversão que deseja realizar: ')
# 
#     if escolha == '1':
#         cel_fahr()
#     
#     if escolha == '2':
#         fahr_cel()