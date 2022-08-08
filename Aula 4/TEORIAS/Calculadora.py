while True:
  try:

    print('- ' * 20)
    print('CALCULADORA SIMPLES DO MATT')
    print('temos as seguintes operações dispiniveis')
    print('- ' * 20)
    print('1 - Multiplicação')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Soma')
    print('- ' * 20)

    conta = int(input('Qual conta deseja realizar? (1, 2, 3 ou 4) '))
    numero1 = float(input('Qual numero deseja usar? '))
    numero2 = float(input('Qual o 2° numero que deseja usar? '))
    
    if(conta == 1):
      print('{} x {} = {}'.format(numero1, numero2, numero1 * numero2))
    elif(conta == 2):
      print('{} - {} = {}'.format(numero1, numero2, numero1 - numero2))
    elif(conta == 3):
      print('{} / {} = {}'.format(numero1, numero2, numero1 / numero2))
    elif(conta == 4):
      print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))
    elif(conta > 4):
      print('operação invalida!')

    saida = int(input('Deseja sair? (1 - Sim | 2 - Não) '))
    if(saida == 2):
      continue
    if(saida == 1):
      break
    else: 
      print('Opção invalida.')
      continue  

  except:
    print('Algo deu errado')
    continue

print('Adios.')
