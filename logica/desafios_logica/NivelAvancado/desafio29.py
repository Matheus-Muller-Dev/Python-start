import zlib

def complexidade_kolmogorov(texto):

    bytes_texto = texto.encode('utf-8')

    texto_comprimento = zlib.compress(bytes_texto)

    return len(texto_comprimento)

texto = "aaaaaaabbbbbcccccdddddddeeeeee"
complexidade = complexidade_kolmogorov(texto)
print(f"Complexidade de Kolmogorov aproximada: {complexidade}")