print('O dia está:')
print('1 - Bom')
print('2 - Ruim')
while True:

  try:
    day = int(input('Como está o dia de hoje? '))
    if(day == 1):
      print('')
      print('Bom dia então meu consagrado!')
      break
    elif(day == 2):
      print('')
      print('Espero que fique tudo bem!')
      break
    else: 
      print('Acorda amigo, escolhe 1 ou 2')
      continue
  
  except ValueError:
    print('Acorda amigo, escolhe 1 ou 2')
  except:
    print('Acorda amigo, escolhe 1 ou 2')

print('Tenha um ótimo dia! Deus te abençoe!')
