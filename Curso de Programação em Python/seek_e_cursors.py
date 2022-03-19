"""
Seek e Cursors

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(118)
print(arquivo.read())

# readline() -> função que lê o arquivo linha a linha

print(arquivo.readline())

# readlines() 

linhas = arquivo.readlines()

print(len(linhas))

"""