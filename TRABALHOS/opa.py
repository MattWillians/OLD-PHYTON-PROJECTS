print('Bem vindo a loja da Andressa Oliveira de Souza ')
vp = float(input('Entre com o valor do produto: '))
quantidadeProduto = int(input('Entre com a quantidade: '))
subtotal = vp * quantidadeProduto

if subtotal < 9:
    valorFinal = subtotal
elif subtotal <= 99:
    valorFinal = subtotal - subtotal * 0.5
elif subtotal <= 999:
    valorFinal = subtotal - subtotal * 0.10
else:
    valorFinal = subtotal - subtotal * 0.15

print('O valor sem desconto: {}'.format(subtotal))
print('O valor com desconto: {}'.format(valorFinal))