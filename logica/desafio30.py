import heapq
from collections import Counter, namedtuple

class NoHuffman(namedtuple("NoHuffman", ["frequencia", "caractere", "esquerda", "direita"])):
    def __lt__(self, outro):
        return self.frequencia < outro.frequencia
    

def construir_arvore_huffman(texto):

    frequencias = Counter(texto)
    heap = [NoHuffman(freq, caractere, None, None) for caractere, freq in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        esquerda = heapq.heappop(heap)
        direita = heapq.heappop(heap)
        novo_no = NoHuffman(esquerda.frequencia + direita.frequencia, None, esquerda, direita)
        heapq.heappush(heap, novo_no)

    return heap[0]

def gerar_codigos(no, prefixo="", codigo={}):
    if no is None:
        return
    
    if no.caractere is not None:
        codigo[no.caractere] = prefixo
    else:

        gerar_codigos(no.esquerda, prefixo + "0", codigo)
        gerar_codigos(no.direita, prefixo + "1", codigo)

        return codigo
    
def codificar_texto(texto):
    arvore = construir_arvore_huffman(texto)
    codigos = gerar_codigos(arvore)
    texto_codificado = "".join(codigos[caractere] for caractere in texto)
    return texto_codificado, codigos

def decodificar_texto(texto_codificado, codigos):
    codigo_invertido = {v: k for k, v in codigos.items()}
    texto_decodificado = ""
    buffer = ""
    for bit in texto_codificado:
        buffer += bit
        if buffer in codigo_invertido:
            texto_decodificado += codigo_invertido[buffer]
            buffer = ""
    return texto_decodificado

texto = "Exemplo de texto para compressão usando Huffman"
texto_codificado, codigos = codificar_texto(texto)
print("Texto Codificado:", texto_codificado)
print("Codigos de Huffman:", codigos)

texto_decodificado = decodificar_texto(texto_codificado, codigos)
print("Texto Decodificado:", texto_decodificado)