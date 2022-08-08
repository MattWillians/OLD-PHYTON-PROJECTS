#------------MENU DE OPÇÕES----------------
print('')
print('Bem vindos a Lanchonete do Matheus  Peireira ')
print('Segue nossa tabela de preços:')
print('')

print('+-------------------------------------------+')
print('| CODIGO|        DESCRIÇÃO      | VALOR (R$)|')
print('| 100   |     Cachorro-Quente   |    9,00   |')
print('| 101   | Cachorro-Quente Duplo |   11,00   |')
print('| 102   |	 X-Egg	        |   12,00   |')
print('| 103   |        X-Salada       |   13,00   |')
print('| 104   |	 X-Bacon    	|   14,00   |')
print('| 105   |	 X-Tudo         |   17,00   |')
print('| 200   |   Refrigerante Lata   |    5,00   |')
print('| 201   |        Chá Gelado     |    4,00   |')
print('+-------------------------------------------+')
#----------------------FIM DO MENU-----------------------
total_a_pagar  = 0

while True:
  #----------VERIFICAR O QUE FOI PEDIDO--------------
  codigo_produto = int(input('Qual dos itens acima você deseja? '))

  if(codigo_produto == 100):
    print('Cachorro-Quente adicionado ao carrinho.\n')
    total_a_pagar += 9.00

  elif(codigo_produto == 101):
    print('Cachorro-Quente-Duplo adicionado ao carrinho.\n')
    total_a_pagar += 11.00

  elif(codigo_produto == 102):
    print('X-Egg adicionado ao carrinho.\\n')
    total_a_pagar += 12.00

  elif(codigo_produto == 103):
    print('X-Salada adicionado ao carrinho.\n')
    total_a_pagar += 13.00

  elif(codigo_produto == 104):
    print('X-Bacon adicionado ao carrinho.\n')
    total_a_pagar += 14.00

  elif(codigo_produto == 105):
    print('X-Tudo adicionado ao carrinho.\n')
    total_a_pagar += 17.00

  elif(codigo_produto == 200):
    print('Refrigerante Lata adicionado ao carrinho.\n')
    total_a_pagar += 5.00

  elif(codigo_produto == 201):
    print('Chá Gelado adicionado ao carrinho.\n')
    total_a_pagar += 9.00
    #VERIFICAR SE O QUE FOI PEDIDO EXISTE 
  else:
    print('Codigo de produto inexistente, digite uma opção válida.')
    continue
    #FIM DA VERIFICAÇÃO

    #PEDIR MAIS ITENS
  mais_pedidos = input('Deseja fazer mais algum pedido? \n Use: S para SIM | e N para NÃO \n')
  if(mais_pedidos.lower() == 's' ):
    continue
  elif(mais_pedidos.lower() == 'n'):
    print('')
    break
    #FIM DA PERGUNTA
  #FIM DO LAÇO

# PRINT DA CONTA 
print('Obrigado por comprar na nossa lanchonete')
print('Valor total a pagar: {}'.format(total_a_pagar))
print('Encerrando Programa...')