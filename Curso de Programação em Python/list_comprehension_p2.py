"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehencion
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]
 
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(numeros)
print(pares)
print(impares)
