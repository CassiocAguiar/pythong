listag=[]
while True:
    nome=input('digite o nome do aluno:')
    nota1=float(input('digite a primeira nota:'))
    nota2=float(input('digite a segunda nota:'))
    media=(nota1+nota2)/2
    listag.append([nome,[nota1,nota2],media])
    c=input('quer continuar?[S/N]').upper().strip()[0]
    while c!='S' and c!='N':
        c=input('quer continuar?[S/N]').upper().strip()[0]
    if c=='N':
        break
print('NO.    NOME    MEDIA')
for i,a in enumerate(listag):
    print(f'{i}     {a[0]}      {a[2]}')
while True:
    opc=int(input('mostrar nota de qual aluno?[999 para interromper]:'))
    if opc==999:
        break
    if opc<=len(listag)-1:
        print(f'notas de {listag[opc][0]} sao {listag[opc][1]}')