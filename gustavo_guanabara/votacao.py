def exibir_menu():
    print("\nBem-vindo  ao sistema de votação!")
    print("Escolha uma das opções abaixo:")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    print("0. Encerrar votação e ver resultados")

def registrar_voto():
    while True:
        try:
            escolha = int(input("\nDigite o número da sua escolha: "))
            if escolha == 0:
                return None
            elif 1 <= escolha <= len(opcoes):
                votos[escolha - 1] += 1
                print(f"Voto registrado para: {opcoes[escolha - 1]}")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à opção.")

def exibir_resultados():
    print("\nResultado da votação:")
    for i, opcao in enumerate(opcoes):
        print(f"{opcao}: {votos[i]} votos")
    vencedor = max(range(len(votos)), key=votos.__getitem__)
    print(f"\nVencedor: {opcoes[vencedor]} com {votos[vencedor]} votos!")


# Definindo as opções de votação
opcoes = ['Zé alfredo', 'Homem de ferro', 'Naruto hokage']
votos = [0] * len(opcoes)

while True:
    exibir_menu()
    if not registrar_voto():
        break

exibir_resultados()
