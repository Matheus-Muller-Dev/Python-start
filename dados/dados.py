import random 

def rolar_dado(numero_faces=6):
    """"Função para rolar um dado com o número especifico de faces (padrão é 6)"""
    return random.randint(1, numero_faces)

def simulador_de_dados():
    while True:

        try:
            numero_faces = int(input("Digite o número de faces do (ou 0 para sair): "))
            if numero_faces == 0:
                print("Saindo do simulador de dados.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        resultado = rolar_dado(numero_faces)
        print(f"O resultado do dado de {numero_faces} faces foi: {resultado}")

        rolar_novamente = input("Deseja rolar o dado novamente? (s/n): ").lower()
        if rolar_novamente != 's':
            print ("Saindo do simulador de dados.")
            break

if __name__ == "__main__":
    simulador_de_dados()