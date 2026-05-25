lista=[]
listap=[]
listaim=[]
while True:
    num=int(input('digite um numero:'))
    lista.append(num)
    c=input('quer continuar?[S/N]:').upper().strip()
    while c!='S' and c!='N':
        c=input('invalido,apenas [S/N]:')
    if c=='N':
        print('Finalizando...')
        break
    else:
        print('Continuando')
    if num%2==0:
        listap.append(num)
    else:
        listaim.append(num)
print(f'lista inteira:{lista}')
print(f'lista apenas de numeros pares:{listap}')
print(f'lista apenas de numeros impares:{listaim}')