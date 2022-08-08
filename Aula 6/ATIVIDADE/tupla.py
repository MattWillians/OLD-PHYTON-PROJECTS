palavras = ('Sam', 'Armstrong', 'Komi', 'Tadano', 'Najime')

for achar_palavras in palavras:
  print('\nPalavras: {} Vogais: '.format(achar_palavras.upper()), end='')
  for letra in achar_palavras:
    if letra.lower() in 'aeiou':
      print(letra.upper(), end="")