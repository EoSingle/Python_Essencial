"""
List Comprehesion

- Utilizando List Comprehesion nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehesion

[dado for dado in iterável]

"""

# Exemplos

numeros = [1, 2, 3, 4, 5]
print(numeros)

res = [numero * 10 for numero in numeros]
print(res)

