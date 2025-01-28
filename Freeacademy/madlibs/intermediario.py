import random

templates = [
    "Ontem eu {verbo_passado} um {substantivo} muito {adjetivo}, e ele disse que {verbo_presente} era {algo_incrivel}.",
    "No futuro, as pessoas vão {verbo_presente} {substantivo_plural} para {atividade}, mas apenas se forem muito {adjetivo}.",
    "Eu sempre {verbo_passado} {substantivo_plural} quando estou {emocao}. Isso me faz sentir {adjetivo}!",
    "Uma vez, durante as férias, um {substantivo} {verbo_passado} em minha direção enquanto eu estava {atividade} com um {outro_substantivo}.",
    "{nome_proprio} disse: '{algo_incrivel}' enquanto {verbo_presente} pelo parque, carregando um {substantivo} muito {adjetivo}."
]

def collect_inputs():
    palavras = {}
    print("\nPor favor, forneça algumas palavras para criar sua história:\n")
    palavras["verbo_passado"] = input("Digite um verbo no passado (ex: correu): ")
    palavras["verbo_presente"] = input("Digite um verbo no presente (ex: come): ")
    palavras["substantivo"] = input("Digite um substantivo (ex: cachorro): ")
    palavras["substantivo_plural"] = input("Digite um substantivo no plural (ex: livros): ")
    palavras["adjetivo"] = input("Digite um adjetivo (ex: engraçado): ")
    palavras["atividade"] = input("Digite uma atividade (ex: dançar): ")
    palavras["emocao"] = input("Digite uma emoção (ex: feliz): ")
    palavras["outro_substantivo"] = input("Digite outro substantivo (ex: mochila): ")
    palavras["nome_proprio"] = input("Digite um nome próprio (ex: Matheus): ")
    palavras["algo_incrivel"] = input("Digite algo incrível (ex: Eu sou um gênio!): ")
    return palavras

def gerar_madlibs(palavras):
    template_escolhido = random.choice(templates)
    historia = template_escolhido.format(**palavras)
    return historia

def main():
    print("Bem-vindo ao Madlibs avançado!")
    continuar = True

    while continuar:
        palavras = collect_inputs()
        historia = gerar_madlibs(palavras)
        print("\n-- Sua historia gerada: --\n")
        print(historia)
        print("\n--Deseja tentar novamente:? (s/n) --\n")
        resposta = input().lower()
        if resposta != "s":
           continuar = False
           print("Obrigado por jogar! Até a proxima.")

if __name__ == "__main__":
    main()
        