"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória


def quadrado(num):
    return num**2


print(quadrado(3))
print(quadrado())


def exponencial (numero, potencia=2):
    return numero**potencia


print(exponencial(2,3)) # 2 * 2 * 2 = 8
print(exponencial(3,2)) # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3,5)) # Eleva à potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será distribuído ao parâmetro numero e o segundo ao parâmetro potencia. Então
# será calculada esta potência

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.
 
# ERRO!
def teste (potencia, num= 2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=0, num2=0):
    return num1 + num2


print(soma(2, 2))
print(soma())
print(soma(10))

# Exemplo mais complexo


def mostra_informacoes(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-Vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacoes())
print(mostra_informacoes(instrutor=True))
print(mostra_informacoes('Ozzy'))
print(mostra_informacoes(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc.

"""

