# VALORES FINAIS VAZIOS PARA EVITAR ERRO DE CALCULO POR PARTE DO PROGRAMA
valor = 0
multiplicador = 0
multiplicador_rota = 0

#IDENTIFICADOR PESSOAL
print('Logistica de Matheus Willians de Paula Pereira \n')

#CALCULO DAS DIMENSÕES DO OBJETO
def dimensoesObjeto():
  #MENU DE OPÇÕES
  global valor
  print('Dimensões VS Valores')
  print('Dimensões               | Valor (R$)')
  print('Até 1000	        |     10')
  print('Entre 1001 e 10000 	|     20')
  print('Entre 10001 e 30000	|     30')
  print('Entre 30001 e 100000	|     50')
  print('Acima 100000	        | Não é aceito\n')
  #FIM DO MENU

  while True:
    #INICIO DE UM LAÇO PARA PERGUNTAS E ERROS
    try:#CASO O USUARIO ERRAR, REPETIR A PERGUNTA
      altura = float(input('Digite a altura do objeto (em cm): '))
      largura = float(input('Digite a largura do objeto (em cm): '))
      comprimento = float(input('Digite o comprimento do objeto (em cm): '))
      dimensao = (altura * largura * comprimento) #FORMULA DE VOLUME TOTAL
    except:#ERRO DE DIGITAÇÃO
      print(' Alguma coisa digitada não é um numero... tente novamente')
      continue
    #TRANSFORMANDO VOLUME EM PREÇO
    else:
      if(dimensao > 100000):#TRATAMENTO DE TAMANHO 
        print('Objeto grande demais! Digite um tamanho toleravel.')
        continue
      elif(dimensao <= 1000):
        valor += 10
      elif(dimensao <= 10000):
        valor += 20
      elif(dimensao <= 30000):
        valor += 30
      elif(dimensao <= 100000):
        valor += 50
      break
  return dimensao #RETORNA O VALOR FINAL PARA VARIAVEL

#DEFINIR O PESO DO OBJETO
def pesoObjeto():
  global multiplicador
  #MENU DE OPÇÕES
  print('')
  print('Peso VS Multiplicador')
  print('Peso(kg)         | Multiplicador')
  print('Até 0.1          |       1')
  print('Entre 0.11 e 1   |      1.5')
  print('Entre 1.10 e 10  |       2')
  print('Entre 10.1 e 30  |       3')
  print('Acima de 30      | Não é aceito\n')

  #LAÇO QUE TRANSFORMA PESO EM MULTIPLICADOR
  while True:
    try:#VERIFICA SE O PESO ESTA DENTRO DAS POSSIVEIS OPÇÕES
      peso = float(input('Qual o peso do objeto? (em Kg) '))
      if(peso <= 0.1):
        multiplicador += 1
      elif(peso <= 1):
        multiplicador += 1.5
      elif(peso <= 10):
        multiplicador += 2
      elif(peso <= 30):
        multiplicador += 3
      else:#TRATAMENTO DE SOBRE-PRESO
        print('Objeto muito pesado!')
        continue
    except:#TRATAMENTO DE ERRO DE DIGITAÇÃO
      print(' Alguma coisa digitada não é um numero... tente novamente')
      continue
    else:
      break
  return peso #retorna o valor do peso

#LAÇO QUE DEFINE O MULTIPLICADOR COM BASE NA ROTA
def rotaObjeto():
  global multiplicador_rota
  # MENU DE ROTAS
  print('             Rotas                   | Multiplicador')
  print(' SB - De São Paulo até Brasília      |	     1.2')
  print(' BR - De Brasília até Rio de Janeiro |	     1.5')
  print(' RB - Rio de Janeiro até Brasília    |      1.5\n')
  
  #LAÇO DE REPETIÇÃO PARA CASO OCORRA ERROS
  while True:
    rota = input('Escolha uma das 3 rotas: ')
    # Aqui eu fiz um tratamento especial usando Upper e Lower.
    if(rota.lower() == 'sb'):
      multiplicador_rota += 1.2
      break
    elif(rota.lower() == 'br'):
      multiplicador_rota += 1.5
      break
    elif(rota.lower() == 'rb'): 
      multiplicador_rota += 1.5
      break
    else:#rota inexistente
      print('Rota invalida!')
      continue
  return rota #retorna o multiplicador da roda desejada

#ATIVAR AS FUNÇÕES
print(dimensoesObjeto())
print(pesoObjeto())
print(rotaObjeto())

#PRINT FINAL
print('Calculando valor do transporte...')
print('Total a pagar pelo transporte: {:.2f}'.format(valor * multiplicador * multiplicador_rota))