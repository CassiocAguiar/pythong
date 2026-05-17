n=1
par=0
impar=0
while n!=0:
    n=int(input('digite um valor:'))
    if n!=0:
        if n%2==0:
            par=par+1
        else:
            impar=impar+1
print('ACABOU')
print(f'voce digitous {par} numeros pares e {impar} numeros impares')