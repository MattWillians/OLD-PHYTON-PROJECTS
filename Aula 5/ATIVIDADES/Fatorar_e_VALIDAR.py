def fator_positivo (pergunta, val_min, valor_max ):
  pergunta = int(input(pergunta))
  while((pergunta < val_min) or (pergunta > valor_max)):
    pergunta = int(input('DIGITE UM NUMERO INTEIRO POSITIVO: '))
  return pergunta

def fatorar(numero):
  """
  Explicação das Funções a seguir:
  |def fatorar(numero):| DEFINIR A FATORAÇÃO DE UM NUMERO ESCOLHIDO PELO USUARIO.
  |      fator = 1     | Na matéria de fatoração, toda fatoração por ZERO é igual a 1.
  |  if(numero == 0):  | Se o numero digitado for ZERO retorne o resultado como 1.
  | for fatoriar in range(1, numero + 1, 1): | PARA FATORIAR UM NUMERO DENTRO DE: 1 até NUMERO ESCOLHIDO, DE UM EM UM.
  | fator *= fatoriar  | Multiplique o valor escolhido pelo seu tamanho para obter seu resultado.
  """
  fator = 1
  if(numero == 0):
    return fator
  for fatoriar in range(1, numero + 1, 1):
    fator *= fatoriar 
  return fator

pergunta = fator_positivo('numero para fatorar: ', 0, 9999)
print('a fatoração de {} é igual à: {}'.format(pergunta, fatorar(pergunta)))
help(fatorar)
