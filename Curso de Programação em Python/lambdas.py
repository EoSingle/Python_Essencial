"""
Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Função em Python

def soma (a, b):
    return a + b


# Expressão em Lambda


lambda x: 3 * x + 1


# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Expressão lambda com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title()+' '+sobrenome.strip().title()

name = input('Seu nome:')
lastname = (input('Seu Sobrenome: '))

print(nome_completo(name, lastname))

# Sintaxe

n = lambda x1, x2, x3, ..., xn: <expressão>
"""

