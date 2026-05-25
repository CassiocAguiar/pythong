lista=[]
c=''
while True:
    valor=int(input('digite um numero:'))
    if valor not in  lista:
        lista.append(valor)
    else:
        print('Finalizando...numero repetido')
        break  
    c=input('quer continuar[S/N]:').upper().strip()
    while c!='S' and c!='N':
        c=input('quer continuar[S/N]:').upper().strip()
    if c=='S':
        print('Continuando...')
    if c=='N':
        print('Finalizando...')
        break 
lista.sort()
print(lista)