"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que á estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo 1

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior
print(numeros)

# Adicionando parâmetros ao sorted ()

print(sorted(numeros, reverse=True)) #Ordena do maior para o menor
"""

# Exemplo 2 - Mais complexo

# Ordenando músicas do álbum MDT do Matuê:

musicas = [
    {'titulo': 'Cogulândia', 'tocou': 24097979},
    {'titulo': 'Antes', 'tocou': 32437160},
    {'titulo': 'Gorilla Roxo', 'tocou': 48191850},
    {'titulo': 'Vem Chapar', 'tocou': 11064644},
    {'titulo': '777-666', 'tocou': 93032372},
    {'titulo': 'É Sal', 'tocou': 62384888},
    {'titulo': 'Máquina do Tempo', 'tocou': 80197721}
]

# Ordenando da menos tocada para a mais tocada

mintomore = sorted(musicas, key=lambda musica: musica['tocou'])
# Ordenando da mais tocada para a menos tocada

moretomin = sorted(musicas, key=lambda musica: musica['tocou'], reverse=True)

# Teste

print('Album MDT por ordem de visualizações:')
for dicts in moretomin:
    print(f"Música: {dicts['titulo']}   Vezes tocada: {dicts['tocou']}")
