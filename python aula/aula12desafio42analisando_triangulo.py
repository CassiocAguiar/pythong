l1=int(input('digite um dos lados do triangulo:'))
l2=int(input('digite outro lado do triangulo:'))
l3=int(input('diigite o outro lado do triangulo:'))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print('eh possivel formar um triangulo')
    if l1==l2 and l2==l3 and l3==l1:
        print('triangulo equilatero')
    elif l1==l2 or l2==l3 or l3==l1:
        print('triangulo isosceles')
    else:
        print('triangulo escaleno')
else:
    print('nao eh possivel formar um triangulo')