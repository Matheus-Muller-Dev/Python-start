qtidade = float(input("Informe a quantidade de carros: "))
valor = float(input("Informe o valor da locação: "))

fmensal = qtidade * valor
fanual = (float(qtidade * 0.8) * valor) * 12

fmensal = int(fmensal)
fanual = int(fanual)

print("O faturamento mensal é de: " + str(fmensal))
print("O faturamento anual considerando a locação de 80% é de: " + str(fanual))
