"""
Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh e para cada habitante entre com os seguintes dados:
Consumo do mês e o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial). 
No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor.
"""
import os

cont = 1
s_rsd = 0
s_cmr = 0
s_ind = 0
c_maior = 0
c_menor = 99999
c_total = 0

print('==================================================================')
print('')
print('             SISTEMA DE CONTAS DE LUZ DA CEMIG')
print('')
print('==================================================================')
print('')

print('Qual o nome do município?')
name_mncp = str(input(''))
print(f'Qual o número de habitantes de {name_mncp}?')
n_hab = int(input(''))
print(f'Qual o valor do kWh residencial de {name_mncp}?')
v_kwh_rsd = float(input('R$'))
print(f'Qual o valor do kWh comercial de {name_mncp}?')
v_kwh_cmr = float(input('R$'))
print(f'Qual o valor do kWh industrial de {name_mncp}?')
v_kwh_ind = float(input('R$'))
os.system('cls') or None

while cont <= n_hab:
    print(f'Qual o consumo do mês em kWh do habitante [{cont}/{n_hab}] ?')
    c_hab = float(input(''))
    print('Qual o tipo de consumidor?')
    print('[1] Residencial')
    print('[2] Comercial')
    print('[3] Industrial')
    t_hab = int(input(''))
    os.system('cls') or None
    if t_hab == 1:
        s_rsd = s_rsd + c_hab
    elif t_hab == 2:
        s_cmr = s_cmr + c_hab
    elif t_hab == 3:
        s_ind = s_ind + c_hab
    
    if c_hab > c_maior:
        c_maior = c_hab
    if c_hab < c_menor:
        c_menor = c_hab
    
    c_total = c_total + c_hab
    cont += 1

c_med = c_total / n_hab
rsd_total = s_rsd * v_kwh_rsd
cmr_total = s_cmr * v_kwh_cmr
ind_total = s_ind * v_kwh_ind
v_total = rsd_total + cmr_total + ind_total

print('              BOLETIM FINAL DE CONSUMO')
print('')
print('')
print(f'O maior consumo da cidade foi de {c_maior}kWh.')
print(f'O menor consumo da cidade foi de {c_menor}kWh.')
print(f'A média de consumo da cidade foi de {c_med:.2f}kWh por habitante.')
print('')
print(f'Total de kWh Residencial: {s_rsd}')
print(f'Total arrecadado Residencial: R${rsd_total:.2f}')
print(f'Total de kWh Comercial: {s_cmr}')
print(f'Total arrecadado Comercial: R${cmr_total:.2f}')
print(f'Total de kWh Industrial: {s_ind}')
print(f'Total arrecadado Industrial: R${ind_total:.2f}')
print('')
print(f'O valor total arrecadado foi R${v_total:.2f}')
