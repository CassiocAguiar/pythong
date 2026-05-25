lista=[]
while True:
    num=int(input('digite um numero:'))
    lista.append(num)
    c=input('quer continuar?[S/N]:').upper().strip()[0]
    while c!='S' and c!='N':
        c=input('por favor,apenas [S/N]:').upper().strip()[0]
    if c=='N':
        print('Finalizando...')
        break
    else:
        print('Continuando')
print(f'quantidade de numeros digitados:{len(lista)}')
lista.sort(reverse=True)
print(f'lista em ordem decrescente:{lista}')
if 5 in lista:
    print('o numero 5 foi digitado e esta na lista')
    print('posicoes ',end='')
else:
    print('o numero 5 nao foi digitado e nao esta lista')
for pos,cin in enumerate(lista):
    if cin==5:
        print(pos)

    
