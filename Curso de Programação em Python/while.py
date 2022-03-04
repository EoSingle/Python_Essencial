cont = 1
num = int(input('Tabuada de: '))
lmt = int(input(f'Tabuada de {num} até: '))

while cont <= lmt:
    x = cont * num
    print(f'{num} x {cont} = {x}')
    cont += 1
