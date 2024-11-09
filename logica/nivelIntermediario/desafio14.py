def palidromo(s):
    s = s.lower().replace("", "") # Converte para minúsculas e remove espaços
    return s == s[::-1] # /Gera uma string invertida.

texto = "asa"
if palidromo(texto):
    print("É um palídromo!")
else:
    print("Não é um palídromo.")
