"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

# Else -> É executado somente se não ocorrer erro.

try: 
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor inválido.')
else:
    print(f'Você digitou {num}')

# Finally

try: 
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor inválido.')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a,b):
    return a / b

num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except:
    ('Valor inválido, digite um número inteiro.')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO

def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError: 
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o primeiro número: ')

print(dividir(num1, num2))

# Exemplo de tratamento genérico

def dividir(a,b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu algum problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o primeiro número: ')

print(dividir(num1, num2))
"""
