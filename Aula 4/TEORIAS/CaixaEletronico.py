valor = int(input('DIGITE O VALOR DA CONTA EM REAIS: '))
print('Para paga sua conta de {} é necessario: '.format(valor))

if(valor >= 100):
  cedulas100 = (valor // 100)
  valor = valor - cedulas100 * 100
  print('{} Cédulas de 100'.format(cedulas100))
if(valor >= 50):
  cedulas50 = (valor // 50)
  valor = valor - cedulas50 * 50
  print('{} Cédulas de 50'.format(cedulas50))
if(valor >= 20):
  cedulas20 = (valor // 20)
  valor = valor - cedulas20 * 20
  print('{} Cédulas de 20'.format(cedulas20))
if(valor >= 10):
  cedulas10 = (valor // 10)
  valor = valor - cedulas10 * 10
  print('{} Cédulas de 10'.format(cedulas10))
if(valor >= 5):
  cedulas5 = (valor // 5)
  valor = valor - cedulas5 * 5
  print('{} Cédulas de 5'.format(cedulas5))
if(valor >= 1):
  cedulas1 = (valor // 1)
  valor = valor - cedulas1 * 1
  print('{} Cédulas de 1'.format(cedulas1))

