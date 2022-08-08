lado1 = float(input('Primeiro lado do triangulo: '))
lado2 = float(input('Segundo lado do triangulo: '))
lado3 = float(input('Terceiro lado do triangulo: '))

if((lado1 == 0) or (lado2 == 0) or (lado3 == 0)):
  print('NENHUM DOS LADOS PODE SER EQUIVALENTE A ZERO')

elif((lado1 + lado2 > lado3) or (lado2 + lado3 > lado1) or (lado1 + lado3 > lado2)):
  print('UM LADO NÃO PODE SER MAIOR QUE A SOMA DE OUTROS 2')

elif(lado1 == lado2 == lado3):
  print('Triangulo Equilatero')

elif((lado1 == lado2 < lado3) or (lado1 > lado3 == lado2) or (lado1 > lado3 < lado2)):
  print('Triangulo Isóceles')

elif(lado1 != lado2 != lado3):
  print('Triangulo Escaleno')

