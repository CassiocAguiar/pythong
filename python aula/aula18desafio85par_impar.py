listat=[]
listapar=[]
listaim=[]
for c in range(1,7+1):
    n=int(input('digite um numero:'))
    if n%2==0:
        listapar.append(n)
    else:
        listaim.append(n)
listapar.sort()
listaim.sort()
listat.append(listaim[:])
listat.append(listapar[:])
print(f'lista numeros impares:{listat[0]}')
print(f'lista numeros pares:{listat[1]}')
