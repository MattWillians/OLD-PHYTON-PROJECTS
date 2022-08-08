def texto(pergunta, min, max):
  text = input(pergunta)
  size = len(text)
  while ((size < min) or (size > max)):
    text = input(pergunta)
    size = len(text)
  return text
  
resposta = texto('Digite uma frase: ', 10, 30)
print('A frase {} esta dentro dos parametros {} e {} \n finalizando sessão...'.format(resposta, 10, 30))