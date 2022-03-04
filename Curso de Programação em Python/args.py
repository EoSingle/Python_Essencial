"""
Entendendo o *args

- O *args é um parametro, como outro qualquer. Isso significa que você poderá chamar de qualquer 
coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos #args para defini-lo

# Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma
tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

    
"""

# Entendendo o *args

from traceback import print_tb


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(5, 6, 4, 1, 2, 4))
