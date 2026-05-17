"""n1=float(input('digite um numero:'))
n2=float(input('digite outro numero:'))
n3=float(input('digite outro numero:'))
menor=n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor=n3
print(f'o menor valor digitado foi {menor}')
maior=n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior=n3
print(f'o maior numero digitado foi {maior}')"""

n1=float(input('digite um numero:'))
n2=float(input('digite outro numero:'))
n3=float(input('digite outro numero:'))
if n1<n2 and n1<n3:
    print(f'menor {n1}')
if n2<n1 and n2<n3:
    print(f'menor {n2}')
if n3<n1 and n3<n2:
    print(f'menor {n3}')
if n1>n2 and n1>n3:
    print(f'maior {n1}')
if n2>n1 and n2>n3:
    print(f'maior {n2}')
if n3>n1 and n3>n2:
    print(f'maior {n3}')
if n1==n2 and n1==n3 and n2==n3:
    print('os numeros sao iguais')