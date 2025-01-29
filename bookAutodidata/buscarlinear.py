nomes = ["Ana", "André", "Beatriz", "Bruno", "Camila", "Carlos", "Daniel", "Daniela", "Eduardo", "Elisa", 
         "Felipe", "Fernanda", "Gabriel", "Gabriela", "Helena", "Henrique", "Isabella", "Igor", "João", "Júlia", 
         "Kevin", "Karina", "Lucas", "Larissa", "Matheus", "Mariana", "Rafael"]

# Peseudocodigo para algoritimo de pesquisa sequencial
# function linearSearch: in ->DAta[], item
# found = -1
# for i in (0 to data.length): if data[i] equals item
#     // item is found in the array
#     // returning the index
#     return i
#     // item not found in the array
#     // -1 means no item found, as negative index is not valid
#     return -1

# busca por indice

def perquisar_por_nome(nome):
    if nome in nomes:
        return f"{nome} está na posição {nomes.index(nome) + 1}."
    return f"{nome} não foi encontrado."

def pesquisar_por_posicao(posicao):
    if 1 <= posicao <= len(nomes):
        return f"O nome na posição {posicao} é {nomes[posicao - 1]}."
    return "Posição invalida"


print(perquisar_por_nome("Bruno")) # Bruno ta na posição 3, mais iteramos mais 1
print(pesquisar_por_posicao(4))