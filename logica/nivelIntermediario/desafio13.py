def soma_serie_geometrica(a, r, n):
    if r == 1: # Se r == 1, a série é constante
        return a * n    
    else:
        return a* (1 - r**n) / (1 - n)
    
# exemplos de uso
a = 3
r = 2
n = 5

soma = soma_serie_geometrica(a, r, n)
print(f"A soma dos {n} primeiros termos da série geométrica é: {soma}")