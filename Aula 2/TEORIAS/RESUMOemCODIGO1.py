#RESUMO EM CODIGO #1
#RITUAL DE INICIAÇÃO
print('Olá, Mundo!')
print(' ')

#TESTE DE VARIAVEIS
nota = 9.5
disciplina = 'matematica'
print(' ')

print(nota)
print(disciplina)
print(' ')

#TESTE COM TEXTOS, CONTAS, CONCATENAÇÃO
print('Olá, este é um teste matematico')
print('teste com contas decimais')
print(' ')

print('A soma de A com B é: ' 'A' + 'B')
print("Sendo A = 23, e B = 45, temos:")
print(23+45)
print(' ')

print('Teste de contas decimais complexas')
print('Sendo: 9 * (27+84)/4, temos:')
print(9*(27+84)/4)
print(' ')

#TESTE DE BOOLEANOS
a = 4
b = 8

print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b) 
print(' ')

#TESTE DE STRINGS
nota2 = 7.5
nota3 = 6.5
nota4 = 10.0

s1 = 'Logica de Programação'
s1 = s1 + ' e Algoritmos'
s2 = 'A' + '-' * 32 + 'B'
s3 = 'Sua nota foi %f na disciplina de Logica de Programação e Algoritmos' % nota2 
s4 = 'Sua nota foi %.1f na disciplina de Logica de Programação e Algoritmos' % nota3
s5 = 'Sua nota foi {} Na disciplina de {}'.format(nota4, s1)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(' ')

#TESTE DE FATIAMENTO
s1_1 = 'Logica de Programação e Algoritmos'

print(s1_1[0:6])
print(s1_1[0:21])
print(' ')

#TESTE DE TAMANHO - LENGHT OU ''LEN''
s1_2 = 'Logica de Programação'
tamanho = len(s1_2)
soma1 = 44

print(tamanho)
print(soma1)
print(tamanho + soma1)
print(' ')

#FUNÇÃO DE ENTRADA: ''DIGITA AQUI''
nome = input('Digite seu nome, por favor ')
idade = input('Digite sua idade, por favor ')
sexo = input('Digite seu Sexo, por favor ')
escola = input('Qual a escola em que você estuda? ')
disciplina1 = input('Digite a disciplina atual, por favor ')
sua_nota = float(input('Digite sua nota com 1 casa decimal, por favor '))
print(' ')

print('Bem vindo {} ao meu sistema'.format(nome))
print('registramos que sua idade é de {} anos'.format(idade))
print('e seu sexo é denominado {}'.format(sexo))
print(' ')
print('Escola atual: {}'.format(escola))
print('Da disciplina vigente {}'.format(disciplina1))
print('sua nota atual é: {}'.format(sua_nota))
print(' ')

#EXERCICIO
num1 = int(input('Digite aqui um numero INTEIRO: '))
num2 = int(input('Digite aqui um segundo numero INTEIRO: '))

print('o resultado da soma de {} com {} é: '.format(num1, num2))
print(num1 + num2)