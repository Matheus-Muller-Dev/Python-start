def mostrar_dados():
    print("=============================")
    print("=== Seja muito bem vindo  ===")
    print("=============================")

    nome = input("==== como é o seu nome? ====: ")

    print("=============================")
    print("==== Prazer em conhecer =====")
    print(f"========= {nome} ===========")
    print("=============================")

    dia = input("===== Qual dia nasceu? ======: ")
    mes = input("===== Qual mês nasceu? ======: ")
    ano = input("===== Qual ano nasceu? ======: ")

    print("========================================")
    print("======= seus dados:  ===================")
    print(f"seu nome: {nome} ")
    print(f"data de nascimento: {dia}/{mes}/{ano}")
    print("========================================")


    resposta = str(input("Deseja continuar colocando dados? "))

    while resposta == 'S':
        return mostrar_dados()
    else: 
        print("Obrigado por usar nosso sistema! Até logo.")

mostrar_dados()