reta1=float(input('digite o comprimento da reta em cm:'))
reta2=float(input('digite o comprimento da reta em cm:'))
reta3=float(input('digite o comprimento da reta em cm:'))
if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    print('eh possivel formar um triangulo')
else:
    print('nao eh possivel formar um triangulo')