"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função


def quadrado(num):
    return num**2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função.

# A ordem dos parâmetros importa!

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Jolie', nome='Angelina'))
"""

# Erro comum na utilização do return


def soma_impares(num):
    total = 0
    for numero in num:
        if numero % 2 != 0:
            total = total + numero
    return total


lista = [1, 2, 3 ,4, 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3 ,4, 5, 6, 7
print(soma_impares(tupla))