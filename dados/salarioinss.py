vhora = float(input("Informe o valor da hora-aula: "))
naulas = float(input("Informe o número de hora-aulas dadas no mês: "))
pdescontos = float(input("Informe o percentual de descontos do INSS: "))

sbruto = vhora * naulas
sliquido = sbruto - (sbruto * pdescontos) / 100

sbruto = int(sbruto)
sliquido = int(sliquido)

print(f"O valor do salário bruto é: " + str(sbruto))
print(f"O valor do salário liquido é: " + str(sliquido))
