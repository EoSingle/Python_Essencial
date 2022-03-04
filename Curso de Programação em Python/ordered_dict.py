"""
Módulo Collections - Ordered Dict

# Em um dicionário, a ordem não é mantida.
dicionario = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

for chave, valor in dicionario.items():
    print(f'Chave= {chave} : Valor= {valor}')

OrderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos.

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5})

for chave, valor in dicionario.items():
    print(f'Chave= {chave} : Valor= {valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários Comuns

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 2, 'a' : 1}

print(dict1 == dict2) # True or False (???)
# True -> Já que a ordem não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a' : 1, 'b' : 2})
odict2 = OrderedDict({'b' : 2, 'a' : 1})
print(odict1 == odict2) # True or False (???)
# False -> Já que a ordem importa para o OrderedDict
"""
