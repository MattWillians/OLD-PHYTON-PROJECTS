cadastro = {'nome':[],'sexo':[],'idade':[]}
lista_mulher_baixo30 = []
idades = []
cadastros = 0
total_idades = 0

while True:
  
  finalizar = input('Deseja sair do cadastro? (s/n)')
  if finalizar.lower() == 's':
    break
  elif finalizar.lower() == 'n':
    nome = input('Qual o seu nome? ')
    sexo = input('Qual o seu sexo? masculino / feminino: ')
    idade = int(input('Qual a sua idade? '))
    idades.append(idade)
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['idade'].append(idade)
    cadastros += 1
    total_idades += 1
    todas_as_idades = sum(idades)
    media_idades = todas_as_idades / total_idades
  else:
    print('DIGITE -> SIM <- ou -> NÃO <-')
    continue

  if sexo.lower() == 'feminino':
    if idade < 30:
      lista_mulher_baixo30.append(nome)

print('Total de cadastros: {}'.format(cadastros))
print('Media de idade dos cadastrados: {}'.format(media_idades))
print('Mulheres com menos de 30 anos: ', lista_mulher_baixo30)
