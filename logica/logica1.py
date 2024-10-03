valorhora_extras = 80
horas_trabalhadas = float(input("Informe as horas trabalhasdas: "))
horas_extra = float(input("Informe o número de horas extras: "))
valor_hora = float(input("Informe o valor da hora: "))

salario_bruto = (horas_trabalhadas + horas_extra * (valorhora_extras/100)) * valor_hora

inss = salario_bruto * (9/100)
fgts = salario_bruto * (8/100)
salario_liquido = salario_bruto - inss

print(f"O salario bruto é {salario_bruto}")
print(f"O salário liquido é: ", salario_liquido)
print(f"O INSS é: {inss}")
print(f"O FGTS é {fgts}")


