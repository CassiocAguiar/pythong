par=0
valores=(int(input('digite um valor:')),int(input('digite um valor:')),int(input('digite um valor:')),int(input('digite um valor:')),)
for v in valores:
    if v%2==0:
        par=par+1
print(f'o numero 9 aparece {valores.count(9)} vezes')
if 3 in valores:
    print(f'o numero 3 aparece na posicao {valores.index(3)+1}')
else:
    print('valor 3 nao foi digitado')
print(f'quantidade de numeros pares:{par}')