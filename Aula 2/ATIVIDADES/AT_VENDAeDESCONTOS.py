print('Algoritmo capaz de calcular e exibir descontos de produtos')
print('- ' * 20)

pro = input('Qual o produto sendo comprado? ')
val = float(input('  Digite o valor constado no produto: '))
des = float(input('    Qual desconto será aplicado no produto? (de 0-100) '))
desr = float(val * (des / 100))
res = val - desr
print('- ' * 20)

s1 = 'Produto Solicitado: {}'.format(pro)
s2 = 'Valor sem desconto: {}'.format(val)
s3 = 'Desconto aplicado: {}'.format(des)
s4 = 'Valor do produto com desconto aplicado: %.2f' % res
print('- ' * 20)

print(s1)
print(s2)
print('- ' * 20)
print(s3)
print(s4)