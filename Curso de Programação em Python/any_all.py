"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

print(all(['a', 'b', 'c', 'd'])) # True
print(all([1, 0, 1, 1, 0, 1])) # False
print(all([])) # True

#OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([1, 0, 0, 0, 1, 2, 4, 5])) # True
print(any([0, 0, 0, 0, 0])) # False

"""

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([ x * 10 for x in range (1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({ x * 10 for x in range (1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range (1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range (1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')
