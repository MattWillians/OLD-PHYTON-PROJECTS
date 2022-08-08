name = ''
while not name:
  name = input('A real name please: ')
value = int(input('Digite um valor que não seja 0: '))
if value:
  print('Aha, boa escolha, {} não é um zero'.format(value))
else:
  print('Poxa, pra que digitar zero?')