# lista de dicionarios, com itens "nome" e "valor"
mercado = [
    {"nome": "amendua", "valor": 3.45},
    {"nome": "chocolate", "valor": 2.49},
    {"nome": "paçoca", "valor": 4.95},
    {"nome": "refrigerante", "valor": 2.50},
    {"nome": "trindent", "valor": 3.50}
]
# Para trocar a lista ordenada e ordenar por valor, trocar em "item[..]"
mercado_ordenado = sorted(mercado, key=lambda item: item["nome"])
mercado_ordenado_reverso = sorted(mercado, key=lambda item: item["nome"], reverse=True)

# lista de palavras, com item "anime"
palavras = [
    {"anime": "one piece"}, 
    {"anime":"Dragon ball"}, 
    {"anime":"One punch man"}, 
    {"anime":"Tokyo Ghoul"}
]
palavras_ordenada = sorted(palavras, key=lambda item: item["anime"])
palavras_ordenada_inversa = sorted(palavras, key=lambda item: item["anime"], reverse=True)

# Saida para verificar lista ordenada
print(palavras_ordenada)
print(" ")
print(palavras_ordenada_inversa)