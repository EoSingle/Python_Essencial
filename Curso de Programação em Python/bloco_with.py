"""
O bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with

"""

# O bloco with

with open (r'Python\Udemy\Curso de Programação em Python\texto.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.readlines())
