from ast import If


idade = int(input('Idade: '))
if(idade > 60):
  print('Você tem direito aos beneficios')

dano_escudo = int(input('Digite o dano: '))
poder_escudo = int(input('Digite o poder do escudo:'))
if(dano_escudo > poder_escudo):
  print('-10 HP')

direction = input('direção: ')
if((direction == 'Norte') or (direction == 'Sul') or (direction == 'leste') or (direction == 'Oeste')):
  print('Você escapou!')

ano = int(input('Qual ano em questão? '))
bisex = (ano % 4)

if(bisex == 0):
  print('Pode ser um ano bisexto')
else:
  print('Não é um ano bisexto')

direcao1 = input('cima ou baixo? ')
direcao2 = input('baixo ou cima? ')

if((direcao1 == direcao2) == True):
  print('Decida-se')
elif((direcao1 == direcao2) == False):
  print('Anda-le!')
