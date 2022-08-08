mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[2][2:5])
print(mochila[0][0:4])
print('')

for item in mochila:
  for letra in item:
    print(letra, end='')
  print()