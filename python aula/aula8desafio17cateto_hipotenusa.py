# from math import sqrt,pow 
import math
ca=float(input('digite o valor do cateto adjascente:'))
co=float(input('digite o valor do cateto oposto:'))
# h=sqrt((pow(ca,2))+(pow(co,2)))
h=math.hypot(ca, co)
print(f'sabendo o cateto adjascente {ca} e o cateto oposto {co} do triangulo retangulo conseguimos obter a hipotenusa {h:.2f}')
