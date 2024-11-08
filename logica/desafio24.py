def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        # Escolhe o pivô (usando o último elemento como exemplo)
        pivot = array[-1]
        left = [x for x in array[:-1] if x <= pivot] # Elementos menores ou iguais ao pivô
        rigth = [x for x in array[:-1] if x > pivot] # Elementos maiores que o pivô

        # Recursivamente aplica o quicksort á esquerda e à direita, depois combina
        return quicksort(left) + [pivot] + quicksort(rigth)

array = [33, 10, 59 , 27, 14, 88, 19, 1]
sorted_array = quicksort(array)
print("Array ordenado:", sorted_array)
