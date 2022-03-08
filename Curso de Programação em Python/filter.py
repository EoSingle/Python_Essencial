"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media:.2f}')

# OBS: Assim como a função map(), a filter recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda x: x < media, dados)
print(type(res))
print(list(res))

# O valor zera depois da primeira utilização, semelhante a função map.

paises= ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)
print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retora um objeto mapeando a função para cada elemento iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando os elementos de acordo com a função.

"""

# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)