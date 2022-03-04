"""
Módulo Collections - Named Tuple

Named Tuple -> São tuplas onde especificamos um nome para a mesma e também parâmetros.
"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2  - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3  - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade = 2, raça= 'Chow-Chow', nome='Ray')

print(cachorro)
# <class '__main__.cachorro'>
print(ray)
# cachorro(idade=2, raça='Chow-Chow', nome='Ray')

# Acessando os dados

# Forma 1

print(ray[0]) # Idade
print(ray[1]) # Raça
print(ray[2]) # Nome

# Forma 2

print(ray.idade) # Idade
print(ray.raça)  # Raça
print(ray.nome)  # Nome
