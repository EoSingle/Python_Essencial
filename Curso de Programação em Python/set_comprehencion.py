"""
Set Comprehension

"""

# Exemplos

numeros = {num for num in range(1,7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range (10)}
print(numeros)

# Refatorando para um dicionário

numeros = {x: x ** 2 for x in range (10)}
print(numeros)

# Pra finalizar 

letras = {letra for letra in 'Geek University'}
print(letras)