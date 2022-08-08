while True:
  try:
    numero = int(input('Digite um numero legal: '))
    break
  except ValueError:
    print('Poxa, isso não é um numero...')