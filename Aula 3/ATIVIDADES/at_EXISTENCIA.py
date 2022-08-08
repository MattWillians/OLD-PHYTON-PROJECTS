nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))

if(nome == 'Vinicius'):
  print('Bem vindo Vinicius')

elif(idade <= 18):
  print('Você é menor de idade.')

elif(idade >= 100):
  print('Esta pessoa provavelmente não existe.')

else:
  print('Bem vindo {}.'.format(nome))