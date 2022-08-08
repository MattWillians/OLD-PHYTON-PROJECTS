notas_ja_escritas = (0)
notas = (1)

while(notas <= 5):
  nota_escrita = float(input('Digite sua {}° nota: '.format(notas)))
  notas_ja_escritas += nota_escrita
  notas += 1
media = notas_ja_escritas / 5
if(media < 7):
  print('REPROVAAADO')
else:
  print('FOI SORTE.')