# ------------> MENU DE OPÇÕES <------------=
print('')
print('Bem vindo a Loja Atacadista do Matheus Pereira \n')
print('__________________________________')
print('   QUANTIDADES    |   DESCONTOS   ')
print('Até 9             | 0% na unidade ')
print('Entre 10 e 99     | 5% na Unidade ')
print('Entre 100 e 999   | 10% na Unidade')
print('De 1000 para mais | 15% na Unidade \n')
# -----------> FIM DO MENU DE OPÇÕES <----------------------

valor_produto = float(input('Digite o valor unitário do produto: ')) #SALVA O VALOR DO PRODUTO
qtd_produto = int(input('Digite a quantidade que será comprada: ')) #SALVA A QUANTIDADE UNITARIA A SER COMRPRADA
print('')
valor_sem_desconto = (valor_produto * qtd_produto) # TOTAL A PAGAR BRUTO

if(qtd_produto <= 9): 

  # -------------CONTA---------------- 
  print('    UNIDADES - DESCONTO      | TOTAL COM / SEM DESCONTO')
  print('Unidades compradas: {}        | Total a pagar: {:.2f}'.format(qtd_produto, valor_sem_desconto))
  print('Desconto: -> NÃO APLICADO <- | Total de unidades inferior a 10 \n')
  #--------- FIM DA CONTA -------------

elif(qtd_produto <= 99):

  desconto5 = float( valor_sem_desconto * (5 / 100)) #FORMULA DE CALCULO DE DESCONTO 
  valor_final5 = float(valor_sem_desconto - desconto5) #VALOR BRUTO - VALOR DO DESCONTO = VALOR FINAL

   # -------------CONTA----------------
  print('  UNIDADES - DESCONTO    | TOTAL COM / SEM DESCONTO') 
  print('Unidades compradas: {}  | Total sem Desconto aplicado: {:.2f}'.format(qtd_produto, valor_sem_desconto))
  print('Desconto de 5% Aplicado! | Total a pagar: {:.2f} \n'.format(valor_final5))
  #--------- FIM DA CONTA -------------

elif(qtd_produto <= 999):

  desconto10 = float( valor_sem_desconto * (10 / 100))#FORMULA DE CALCULO DE DESCONTO
  valor_final10 = float(valor_sem_desconto - desconto10)#VALOR BRUTO - VALOR DO DESCONTO = VALOR FINAL

   # -------------CONTA----------------
  print('  UNIDADES - DESCONTO     | TOTAL COM / SEM DESCONTO')
  print('Unidades compradas: {}   | Total sem Desconto aplicado: {:.2f}'.format(qtd_produto, valor_sem_desconto))
  print('Desconto de 10% Aplicado! | Total a pagar: {:.2f} \n'.format(valor_final10))
  #--------- FIM DA CONTA -------------

else:
  desconto15 = float( valor_sem_desconto * (15 / 100))#FORMULA DE CALCULO DE DESCONTO
  valor_final15 = float(valor_sem_desconto - desconto15)#VALOR BRUTO - VALOR DO DESCONTO = VALOR FINAL

   # -------------CONTA----------------
  print('    UNIDADES - DESCONTO   | TOTAL COM / SEM DESCONTO')
  print('Unidades compradas: {}  | Total sem Desconto aplicado: {:.2f}'.format(qtd_produto, valor_sem_desconto))
  print('Desconto de 15% Aplicado! | Total a pagar: {:.2f} \n'.format(valor_final15))
  #--------- FIM DA CONTA -------------

# ---------------- PRINT FINAL DE AGRADECIMENTO ------------------
print('Obrigado por comprar na minha loja! Encerrando programa...')