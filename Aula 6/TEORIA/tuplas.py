mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

print(mochila)
print('')
print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])
print('')

# mochila[2] = 'Ovos' 

# #impossivel

for stuff in mochila:
  print('Aqui temos: {}'.format(stuff))
  print('')

mochila_upgrade = ('Calça', 'Espingarda')
mochila_grande = mochila + mochila_upgrade

print(mochila)
print(mochila_upgrade)
print(mochila_grande)

def somatoria(*num):
  somar = 0
  print('Numeros escolhidos: {}'.format(num))
  for number in num:
    somar += number
  return somar

print('Resultado é: {} \n'.format(somatoria(4,4)))
print('Resultado é: {} \n'.format(somatoria(8,16,32)))
