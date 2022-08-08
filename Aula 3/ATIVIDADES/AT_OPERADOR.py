num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('Qual operação deseja fazer? (+, -, * ou /) ')

if(operacao == '+'):
  print(num1 + num2)

elif(operacao == '-'):
  print(num1 - num2)

elif(operacao == '*'):
  print(num1 * num2)

elif(operacao == '/'):
  print(num1 / num2)

else:
  print('Operador não registrado')