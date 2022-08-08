game = {}
jogos = []

for i in range (3):
  game['nome'] = input('Digite o nome do jogo: \n')
  game['desenvolvedora'] = input('Digite a desenvolvedora do mesmo: \n')
  game['ano'] = input('Digite o ano de desenvolvimento: \n')
  jogos.append(game.copy())

for e in jogos:
  for i,j in e.items():
    print('{} é {}'.format(i,j))