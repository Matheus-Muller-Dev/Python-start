nota1 = float(input("Qual foi sua nota no 1 semestre: "))
nota2 = float(input("Qual foi sua nota no 2 semestre: "))
nota3 = float(input("Qual foi sua nota no 3 semestre: "))
nota4 = float(input("Qual foi sua nota no 4 semestre: "))

total = (nota1 + nota2 + nota3 + nota4) // 4

print(
      f"A Media das notas: {nota1:.2f}, {nota2:.2f}, "
      f"{nota3:.2f} e {nota4:.2f} é {total:.2f}"
)
