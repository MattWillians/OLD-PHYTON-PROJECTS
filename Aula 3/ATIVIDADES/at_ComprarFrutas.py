
print('QUITANDA VIRTUAL DO SEU ZÉZIM')
print('-' * 30)
print('Temos as seguintes frutas:')

#PREÇOS
print('1. Maçã | R$ 1.50 cada')
print('2. Laranja | R$ 2.00 cada')
print('3. Banana | R$ 2.10 cada')
print('-' * 30)

#DECSÃO
fruta1 = ('Maçã')
fruta2 = ('Laranja')
fruta3 = ('Banana')
preco_maca = float(2.30)
preco_laranja = float(3.60)
preco_banana = float(1.85)

escolhi = int(input('Qual delas você deseja meu jovem? (1, 2 ou 3): '))

#erro no pedido
while((escolhi <= 0) or (escolhi > 3)):
  
  print('QUITANDA VIRTUAL DO SEU ZÉZIM')
  print('-' * 30)
  print('Temos as seguintes frutas:')

  print('1. Maçã | R$ 1.50 cada')
  print('2. Laranja | R$ 2.00 cada')
  print('3. Banana | R$ 2.10 cada')
  print('-' * 30)
  escolhi = int(input('Digite uma fruta valida (1, 2 ou 3): '))
  print('-' * 30)

if(escolhi == 1):
  unidade = int(input('Quantas unidades você deseja? '))
  total_maca = (preco_maca * unidade)
  print('O total a pagar pela(s) {} é {}'.format(fruta1, total_maca))
else:
  if(escolhi == 2):
    unidade = int(input('Quantas unidades você deseja? '))
    total_laranja = (preco_laranja * unidade)
    print('O total a pagar pela(s) {} é {}'.format(fruta2, total_laranja))
  
  else:
    if(escolhi == 3):
      unidade = int(input('Quantas unidades você deseja? '))
      total_banana = (preco_banana * unidade)
      print('O total a pagar pela(s) {} é {}'.format(fruta3, total_banana))
    else:
      print('produto não existe.')