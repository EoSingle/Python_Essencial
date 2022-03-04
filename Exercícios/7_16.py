"""
Exercício 7.16 - Python

Faça um programa para corrigir uma prova com 10 questões de múltipla escolha (a, b, c, d ou e) em uma turma com 3 alunos. cada questão vale 1 ponto. Leia o gabarito, e
para cada aluno leia sua matricula (número inteiro) e suas respostas. Calcule e escreva: Para cada aluno, escreva sua matrícula, suas respostas e sua nota. O percentual 
de aprovação, assumindo média 7.0.

"""
import os

var = 1
var2 = 1
registro = []

print('===============================================')
print('')
print('            CORRETOR DE AVALIAÇÃO')
print('')
print('================================================')

# Criação Dicionário "Gabarito"

gabarito = {}.fromkeys(range(1,11), 'Vazio')
print(gabarito)

# Adição das opções no gabarito

while var < 11:
    print(f'Digite o gabarito da questão ({var}/10)')
    gab_option = str(input(''))
    gabarito.update({var: gab_option})
    os.system('cls') or None
    print(gabarito)
    var += 1
var = 1

print('Gabarito Finalizado:')
for key, value in gabarito.items():
    print(f'Questão: {key}    Opção: {value}')

# Registro dos alunos e calculo da média

n_alunos = int(input('Número de alunos na turma: '))

while var <= n_alunos:
    media = 0
    print(f'Digite o nome do aluno ({var}/{n_alunos}):')
    name_aluno = str(input(''))
    print(f'Digite a matrícula do aluno "{name_aluno}":')
    mtr_aluno = int(input(''))
    while var2 < 11:
        print(f'Qual a resposta do aluno para a questão {var2}:')
        resposta = str(input(''))
        if resposta == gabarito[var2]:
            media += 1
        var2 +=1
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    registro.extend([(mtr_aluno, name_aluno, media, resultado)])
    var2 = 1
    var +=1

os.system('cls') or None

# Resultado Final

print('Resultado da turma:')
print('Matrícula / Nome do Aluno / Média / Situação')
for indice in registro:
    print(indice)
