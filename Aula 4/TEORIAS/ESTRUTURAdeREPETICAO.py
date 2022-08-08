minimo = int(input('Digite o valor minimo: '))
maximo = int(input('Digite o valor maximo: '))

if(minimo % 2 == 0):
  while(minimo < maximo):
    print(minimo)
    minimo = (minimo * 2)
else: 
  print('tem algo de errado')