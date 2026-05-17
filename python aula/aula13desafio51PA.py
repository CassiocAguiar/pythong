p1= int(input('Enter a Number: '))
razao = int(input('Enter a Divider: '))
deca = p1 + (10 - 1) * razao

for c in range(p1, deca + 1, razao):
    print(f'{c}', end=' -> ')
    
print('END!')