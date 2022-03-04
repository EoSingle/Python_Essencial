"""
Recebendo dados do usuário

Input -> Entrada
"""

print("Qual seu nome? ")
nome = input()

print(f"Seja bem-vindo(a) {nome}")

print("Qual a sua idade?")
idade = int(input())

print(f"O {nome} têm {idade} anos.")
print(f"O {nome} nasceu em {2022 - idade}.")
