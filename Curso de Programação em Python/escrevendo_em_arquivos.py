"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar aa escrita nele. Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos
lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write(). Esta função recebe uma string como parâmetro. Caso contrário teremos
um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir ele será criado, caso ele já exista, o anterior será apagado e um novo será criado.
Dessa forma, todo o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write

# Forma tradicional de escrita em arquivo
arquivo = open('mais.txt', 'w', encoding='utf-8')

arquivo.write('Um texto qualquer./n')
arquivo.write('Mais um texto.')

arquivo.close()

# Forma "Pythônica"

with open('Curso de Programação em Python//novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil./n')
    arquivo.write('Podemos colocar quantas linhas quisermos./n')
    arquivo.write('Mas, esta é a ultima linha.')

with open('geek.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Geek/n' * 100)

"""

with open(r'Curso de Programação em Python\frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
