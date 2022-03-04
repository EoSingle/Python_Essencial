"""
Funções com retorno

- Em python, quando uma função não retorna nenhum valor, o retorno é None.
- Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return.
- Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.

# Exemplo função

#def quadrado_de_7():
#    print(7*7)

#quadrado_de_7()

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a nossa primeira função

def diz_oi():
    return 'Oi '

print(diz_oi())

name = 'Pedro!'

print(diz_oi() + name)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Em uma função podemos ter diferentes returns;
3 - Em uma função podemos retornar qualquer tipo de dado e até múltiplos valores;

# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do return...')
    return 'Oi!'
    print('Estou sendo executado após o return...')


print(diz_oi())

# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:                 # else desnecessário
        return False 
"""
