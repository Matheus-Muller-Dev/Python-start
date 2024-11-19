# n = 5
# for i in range(1, n + 1):
#     print("*" * i)

largura = 5

for i in range(largura // 2, largura + 2, 2):

    for j in range(3, (largura - i // 2) + 1):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end="")

    for j in range(1, (largura - i)):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(largura, 0, -1):

    for j in range(largura - i):
        print(" ", end="")

    for j in range(1, i * 2):
        print("*", end="")
    print()