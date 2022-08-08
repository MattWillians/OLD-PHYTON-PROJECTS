# MENU, FUNÇÃO DE PEDIR, ERRAR, VOLTAR, E VOLTAR PRO MENU.



def testeErro():
  while True:
    print('S - SAIR | N - não sair')
    try:
      teste = input('Ola, digite S ou N pof favor.')
      if teste.upper() == 'S':
        break
      elif teste.upper() == 'N':
        continue
      else:
        print('Algo digitado não condiz com o pedido')
        continue
    except SyntaxError:
      print('Algo digitado não condiz com o pedido')
      continue
    except ValueError:
      print('Algo digitado não condiz com o pedido')
      continue
    except:
      print('Algo digitado não condiz com o pedido')
      continue


#PROGRAMA PRINCIPAL
while True:
  try:
    teste1 = input('Quer iniciar? sim ou não. ')
    if teste1 == 'sim':
      print(testeErro())
    else:
      break
  except:
    continue