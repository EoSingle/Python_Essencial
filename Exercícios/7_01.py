A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(f'Soma: {soma}')

A.pop(4)
A.insert(4, 100)

print('Vetores "A" :')
for valor in A:
    print(valor)
