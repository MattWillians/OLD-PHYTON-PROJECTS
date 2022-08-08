def funcao(numero, ioup):
  if ioup(numero):
    print(numero)

def par(x):
  return (x % 2 == 0)

def impar(y):
  return not par (0)

funcao(10, par)