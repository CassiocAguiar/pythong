matriz=[[0,0,0],[0,0,0],[0,0,0]]
somap=0
somac=0
maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'digite a [{l} {c}]:'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2==0:
            somap=somap+matriz[l][c]
    print()
print(f'soma dos valores pares:{somap}')
for l in range(0,3):
    somac=somac+matriz[l][2]
print(f'soma dos valores da terceira coluna:{somac}')
for c in range(0,3):
    if c==0:
        maior=matriz[1][c]
    elif matriz[1][c]>maior:
        maior=matriz[1][c]
print(f'maior numero da segunda linha:{maior}')

