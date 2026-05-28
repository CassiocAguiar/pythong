d={}
lista=[]
media=0
mediareal=0
while True:
    nome=input('digite o nome:')
    sexo=input('M para masculino,F para feminino[M/F]:').upper().strip()[0]
    while sexo!='M' and sexo!='F':
        sexo=input('por favor,M para masculino,F para feminino[M/F]:').upper().strip()[0]
    idade=int(input('digite a idade:'))
    media=media+idade
    d['nome']=nome
    d['sexo']=sexo
    d['idade']=idade
    lista.append(d.copy())
    c=input('quer continuar?[S/N]:').upper().strip()[0]
    while c!='S' and c!='N':
        c=input('por favor,quer continuar?[S/N]:').upper().strip()[0]
    if c=='N':
        print('Finalizando...')
        break
    else:
        print('Continuando')
print('PESSOAS CADASTRADAS')
print(len(lista))
print('MEDIA DE IDADE DO GRUPO')
print(f'{media/len(lista)}')
print('LISTA COM TODAS AS MULHERES')
for c in lista:
    if c['sexo']=='F':
        print(c['nome'])
print('TODAS AS PESSOAS COM IDADE ACIMA DA MEDIA DO GRUPO')
for p in lista:
    if p['idade']>media/len(lista):
        print(p['nome'])