def borda(texto):
  while True:
    texto = input('Digite uma verdade: ')
    tamanho = len(texto)
    sair = input('Deseja escrever mais verdades? (s/n) ')
    if tamanho:
      print(('+'), ('-' * tamanho), ('+'))
      print(('|'), (texto), ('|'))
      print(('+'), ('-' * tamanho), ('+'))
    if(sair == 'n'):
      break
    else:
      continue
borda(borda)
