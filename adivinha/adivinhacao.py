import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False 

    while not acertou:
        palpite = input("Digite um número entre 1 e 100: ")

        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            acertou = True
            print(f"Parabés! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

if __name__ == "__main__":
    jogo_adivinhacao()