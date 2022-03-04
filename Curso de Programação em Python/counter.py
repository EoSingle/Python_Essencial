"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada 
como parâmetro e como valor a quantidade de ocorrências desse elemento.

# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 5: 5, 2: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = "A matemática é a ciência do raciocínio lógico e abstrato, que estuda através dos números, quantidades, medidas, espaços, estruturas, variações e estatísticas. 
Um trabalho matemático consiste em procurar por padrões, formular conjecturas e, por meio de deduções rigorosas a partir de axiomas e definições, estabelecer novos 
resultados. A matemática desenvolveu-se principalmente na Mesopotâmia, no Egito, na Grécia, na Índia e no Oriente Médio. A partir da Renascença o desenvolvimento da 
matemática intensificou-se na Europa, quando novas descobertas científicas levaram a um crescimento acelerado que dura até os dias de hoje. "

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

"""
from collections import Counter
