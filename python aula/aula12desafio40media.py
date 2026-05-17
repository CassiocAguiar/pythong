n1=float(input('digite sua primeira nota:'))
n2=float(input('digite sua outra nota:'))
media=(n1+n2)/2
if media<5:
    print('Reprovado')
elif media>=5 and media <=6.9:
    print('recuperacao')
else:
    print('Aprovado')
    