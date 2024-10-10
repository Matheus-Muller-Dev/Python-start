from random import choice
import string 

tamanho_senha = int(input("Quantos digitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.punctuation
senha_segura = ''
for i in range(tamanho_senha):
    senha_segura += choice(caracteres)

print("A senha (segura) gerada é: ", senha_segura)