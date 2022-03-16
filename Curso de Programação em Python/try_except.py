"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o origrama pare de funcionar e o usuário receba mensagens de 
erro inesperadas.

A forma geral mais simpes é:

try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Alguma coisa deu errado.')

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Alguma coisa deu errado.')

OBS: Tratar erros de forma genérica não é a melhor opção. O ideal é SEMPRE tratar de forma específica.

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
    
# Podemos tratar vários erros de uma vez

try:
    geek()
except NameError as err1:
    print(f'Deu Name Error: {err1}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print('Alguma coisa deu errado.')

"""

def pega_valor(dicionario,chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    except NameError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic, 5))
