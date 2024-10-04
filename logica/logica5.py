preco = float(input("Qual o preco do produto: "))
p_desconto = float(input("Informe o percentual do desconto: "))

valor_desconto = (preco * p_desconto) / 100
valor_apagar = preco - valor_desconto

print(f"O valor a pagar é: {valor_apagar}")
print(f"O valor do desconto é: {valor_desconto}")
