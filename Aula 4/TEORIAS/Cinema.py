totalpessoas = 0
dineiro = 0

while True:
  print('Para SAIR digite sair.')
  idade = int(input('Qual a idade da(s) pessoa(s) que vai assistir? '))
  saida = input('Deseja adicionar mais pessoas? Se não, digite sair. ')
  if saida == 'sair':
    break
  totalpessoas += 1
  if idade > 3:
    ingresso = (0)
  else:
    if(idade > 12):
      ingresso = (30)
    else:
      ingresso = (15)
  dineiro += ingresso
mediaarrecadada = (totalpessoas / dineiro)
print('Total de pessoas: {}'.format(totalpessoas))
print('Total a pagar: {}'.format(dineiro))
print('Média arrecadada: {}'.format(mediaarrecadada))
