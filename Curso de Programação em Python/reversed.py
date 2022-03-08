"""
Reversed

OBS: 
    - Não confunda com a função reverse() das listas. 
    - A função reverse() só funciona em listas

Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável.
A função reversed() retorna um iterável chamado List Reverse Iterator.
"""

# Exemplos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (Set)   
print(set(reversed(lista)))  # OBS: Em sets, não definimos a ordem dos elementos