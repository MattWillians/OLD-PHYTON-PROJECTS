
meugasto = float(input('Bem vindo a EDP, digite abaixo seu gasto energetico: '))
tipoinstalacao = input('Digite o tipo de instalação (R - RESIDENCIAS, I - INDUSTRIAS e C - COMERCIO) ')

if(tipoinstalacao == 'R'):
  (meugasto <= 500)
  res_baixo = float((meugasto <= 500) * 0.40)
  print('Sua conta de energia é %.2f' %res_baixo)
elif(tipoinstalacao == 'R'):
  (meugasto > 500)
  res_alto = float(meugasto * 0.65)
  print('Sua conta de energia é %.2f' %res_alto)

elif(tipoinstalacao == 'C'):
  (meugasto <= 100)
  come_baixo = float(meugasto * 0.55)
  print('Sua conta de energia é %.2f' %come_baixo)
elif(tipoinstalacao == 'C'):
  (meugasto > 1000)
  come_alto = float(meugasto * 0.60)
  print('Sua conta de energia é %.2f' %come_alto)

elif(tipoinstalacao == 'I'):
  (meugasto <= 5000)
  ind_baixo = float(meugasto * 0.55)
  print('Sua conta de energia é %.2f' %ind_baixo)
elif(tipoinstalacao == 'I'):
  (meugasto > 5000)
  ind_alto = float( meugasto * (0.60))
  print('Sua conta de energia é %.2f' %ind_alto)
else:
  print('O tipo de instalação: {} não existe, ou não é correto'.format(tipoinstalacao))