n1=float(input('digite um valor:'))
n2=float(input('digite outro valor:'))
r=2
while r!=5:
    r=int(input('digite 1 para somar os dois numeros,2 para multiplicar,3 para saber qual eh maior,4 para novos numeros,5 para sair:'))
    if r==1:
        print(f'a soma de {n1} e {n2}={n1+n2}')
    elif r==2:
        print(f'a multiplicacao entre {n1} e {n2}={n1*n2}')
    elif r==3:
        if n1>n2:
            print(f'o n1 eh o maior:{n1}')
        elif n1==n2:
            print('numeros iguais')
        else:
            print(f'o n2 eh o maior:{n2}')
    elif r==4:
        n1=float(input('digite o novo numero que voce quer:'))
        n2=float(input('digite o outro numero novo que voce quer:'))
print('FIM')