import random as randomizer

def opcao(pergunta, min, max):
  pergunta = int(input(pergunta))
  while((pergunta < min) or (pergunta > max)):
    pergunta = int(input('DIGITE UMA DAS OPÇÕES LISTADAS NA TABELA '))
  return pergunta

def vitoria(jogador, cpu):
  global empates, vitoriasPLAYER, vitoriasBOT
  if jogador == 1: #pedra
    if cpu == 1: #pedra
      empates += 1
      print('É UM EMPATE!')
    elif cpu == 2:#papel
      vitoriasBOT += 1
      print('VITÓRIA DO BOT!')
    elif cpu == 3:
      vitoriasPLAYER += 1
      print('VITÓRIA DO PLAYER 1!')

  elif jogador == 2:#papel
    if cpu == 1: #pedra
      vitoriasPLAYER += 1
      print('VITÓRIA DO PLAYER 1!')
    elif cpu == 2:#papel
      empates += 1
    elif cpu == 3:
      vitoriasBOT += 1
      print('VITÓRIA DO BOT!')
  
  elif jogador == 3:
    if cpu == 1: #pedra
      vitoriasBOT += 1
      print('VITÓRIA DO BOT!')
    elif cpu == 2:#papel
      vitoriasPLAYER += 1
      print('VITÓRIA DO PLAYER 1!')
    elif cpu == 3:
      empates += 1
      print('É UM EMPATE!')

  resultados = [vitoriasPLAYER, vitoriasBOT, empates]
  return resultados

print('  PEDRA, PAPEL, TESOURA!         ')

resultados = []
jogadas = []
vitoriasPLAYER = 0
vitoriasBOT = 0
empates = 0

while True: 
  print('  ESCOLHA UM PODER:            ')
  print('0 - SAIR DO JOGO \n 1 - PEDRA! \n  2 - PAPEL! \n   3 - TESOURA!')

  jogadaP1 = opcao('Escolha seu poder: ', 0, 3)
  if jogadaP1 == 0:
    print('Saindo...')
    break

  jogadaCPU = randomizer.randint(1,3)
  jogadas.append([jogadaP1, jogadaCPU])

  for jogada in jogadas:
    for dado in jogada:
      print(dado, end=' ')
    print()
  
  print(vitoria(jogadaP1, jogadaCPU))

print('NUMERO DE VITORIAS DO PLAYER: {}'.format(vitoriasPLAYER))
print('NUMERO DE VITORIAS DO BOT: {}'.format(vitoriasBOT))
print('NUMERO DE EMPATES: {}'.format(empates))  
