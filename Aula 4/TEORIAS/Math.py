while True:
  try:
    comeco = int(input('Qual a primeira tabuada que deseja aprender? '))
    fim = int(input('Qual a ultima tabuada que deseja aprender? '))
    fimtabu = (fim + 1)
    break
  except:
    print('Algo digitado não é um numero, tente novamente.')
    continue
  
for tabuada in range(comeco,fimtabu,1):
  print('TABUADA DO: {}'.format(tabuada))
  for conta in range(comeco,fimtabu,1):
    print('{} x {} = {}'.format(tabuada, conta, tabuada * conta))