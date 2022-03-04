# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

x = 1
valores = []

while x < 7:
    print(f'Digite o valor {x}/6:')
    y = int(input(''))
    valores.append(y)
    x += 1

print(f'Os valores inteiros digitados foram: {valores}')
