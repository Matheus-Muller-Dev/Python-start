lista = [0, 1, 2]
usuario = ''


while usuario not in lista:
    try:
        usuario = int(input('Escolha um número entre 0 e 2: '))
    except ValueError:
        print('Por favor entre com um número')

print(f"Você digitou um valor válido: {usuario}")