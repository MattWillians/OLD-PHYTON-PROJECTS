print('- ' * 30)
print('Hora de ver se passamos de ano!')
print('- ' * 30)

aprovacao = (7)
notamateria1 = float(input('Digite sua 1° nota aqui: '))
notamateria2 = float(input('Digite sua 2° nota aqui: '))
notamateria3 = float(input('Digite sua 3° nota aqui: '))
print('- ' * 30)

if(notamateria1 >= aprovacao):
  print('Aprovado na materia 1 com {} pontos'.format(notamateria1))
else:
  print('Reprovado na materia 1')

if(notamateria2 >= aprovacao):
  print('Aprovado na materia 2 com {} pontos'.format(notamateria2))
else:
  print('Reprovado na Materia 2')

if(notamateria3 >= aprovacao):
  print('Aprovado na materia 3 com {} pontos'.format(notamateria3))
else:
  print('Reprovado na materia 3')
print('- ' * 30)

if(notamateria1 >= aprovacao and notamateria2 >= aprovacao and notamateria3 >= aprovacao):
  print('Aprovação geral')
else:
  print('Reprovação geral')
  print('- ' * 30)