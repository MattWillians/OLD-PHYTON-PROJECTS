def divisao():
  try:
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite um segundo numero: '))
    divida = (numero1 / numero2)
    print('o resultado da divisão de {} com {} é: {}'.format(numero1, numero2, divida))
  except SyntaxError:
    print(' Alguma coisa digitada não é um numero... tente novamente')
  except ZeroDivisionError:
    print('Divisões por 0 não são possiveis...')
  else:
    return divida
  finally:
    print('Até logo')
print(divisao())