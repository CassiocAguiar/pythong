primeiro=int(input('digite o primeiro termo da pa:'))
razao=int(input('digite a razao dessa pa:'))
termo=primeiro
t=0
print('10 PRIMEIROS NUMEROS DA PA')
while t!=10:
    print(termo,end='-')
    termo+=razao
    t+=1
    
