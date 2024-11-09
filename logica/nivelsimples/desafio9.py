# Sistema basico para calcular o IMC
peso = float(input("Qual o seu peso atual: "))
altura = float(input("Qual é a sua altura: "))

# processamento de dados
imc = peso / (altura * altura)

print('Seu IMC é: {0}'.format(imc))

# Estrutura condicional
if imc <= 18.5:
    print('Você esta muito abixo do peso!')
elif imc > 18.5 and imc <= 24.9:
    print('Você está no peso ideal!')
elif imc > 24.9 and imc <= 29.9:
    print('Você está levemente acima do peso!')
else: 
    print('Você está com obesidade')

