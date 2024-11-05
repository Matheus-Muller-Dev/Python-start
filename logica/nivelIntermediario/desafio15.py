# Versão recursiva
def mdc(a, b):
  return a if not b else mdc(b, a % b)

print(mdc(70, 25))
