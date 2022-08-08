supermario = {'jogo': 'Super Mario Bros',
              'desenvolvedora': 'Nintendo',
              'Ano:': 1990}

print(supermario)

print(supermario['jogo'])
print(supermario['desenvolvedora'])
print(supermario['Ano:'])
print('')
print(supermario.values())
print(supermario.keys())
print(supermario.items())

for i in supermario.values():
  print(i)
for o in supermario.keys():
  print(o)
for p in supermario.items():
  print(p)
for n,i in supermario.items():
  print('{} = {}'.format(n,i))

item = input('qual item deseja encontrar? ')
supermario.find(item)