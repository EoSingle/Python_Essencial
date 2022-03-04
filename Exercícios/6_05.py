soma = 0
x = 1

print('Soma de 10 números!')

while x < 11:
    num = int(input(f'Digite o número {x}/10: '))
    soma = soma + num
    x += 1

print (f'A soma dos 10 números digitados foi: {soma}')
