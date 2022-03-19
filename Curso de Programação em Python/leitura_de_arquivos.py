"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'.

open() -> A forma mais simples de utilização nós passamos apenas um parâmetro de entrada que neste caso é o nome do arquivo a ser lido. Essa função 
retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# Utilização:

open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNoteFoundError

# Modos de abertura:

'r' -> open for reading (default)

'w' -> open for writing, truncating the file first

'x' -> open for exclusive creation, failing if the file already exists

'a' -> open for writing, appending to the end of file if it exists

'b' -> binary mode

't' -> text mode (default)

'+' -> open for updating (reading and writing)

<_io.TextIOWrapper name='Python\\Udemy\\Curso de Programação em Python\\texto.txt' mode='r' encoding='utf-8'>

# Exemplo

arquivo = open(r'texto.txt', 'r', encoding='utf-8') # Caminho incompleto devido a conflito de backslash

# OBS: O caminho de um arquivo no Windowns gera conflito com o Python devido ao backslash, para contornar esse erro, você precisa prefixar a string com um r,
para indicar ao interpretador Python que a string deve ser analisada de forma "crua" (o r é de raw string).

print(arquivo)
print(type(arquivo))

# Para ler o conteúdo de um arquivo, após a sua abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o nosso programa. Essa conexão é chamada
de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()
"""

# Passos para se trabalhar com um arquivo

# 1 -> Abrir o arquivo:
arquivo = open(r'Python\Udemy\Curso de Programação em Python\texto.txt', 'r', encoding='utf-8')

# 2 -> Trabalhar com o arquivo:
print(arquivo.read())

# 3 -> Fechar o arquivo:
arquivo.close()

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado. Retorna True se fechado ou False se aberto.

# OBS: Se tentarmos manipular o arquivo após seu fechamento teremos ValueError

