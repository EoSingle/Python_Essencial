"""
Debugando com PDB

PDB -> Python Debugger

# OBS: A utilização do print() para debugar código é uma prática ruim.

def dividir(a,b):
    print(f'a={a} b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err: 
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug' utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB - Python Debugger

# Exemplo com o PDB - Python Debugger - Exemplo 1

# Para utilizar o Python debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Lucas'
sobrenome = 'Albano'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com o PDB - Python Debugger - Exemplo 2

nome = 'Lucas'
sobrenome = 'Albano'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato? 
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas no início do arquivo. Por isso, ao invés de
# colocarmos o import pdb no início do arquivo, nós colocamos somente onde vamos debugar, e ao finalizar já fazemos a remoção.

OBS: A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in (integrada)
chamada breakpoint()
"""