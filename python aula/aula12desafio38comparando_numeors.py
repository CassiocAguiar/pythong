n1=float(input('digite um numero:'))
n2=float(input('digite outro numero:'))
if n1>n2:
    print(f'o primeiro valor eh o maior:{n1}')
elif n2>n1:
    print(f'o segundo valor eh o maior:{n2}')
else:
    print('nao existe maior valor,os dois sao iguais')