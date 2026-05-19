soma=0
q=0
while True:
    n=int(input('digite um numero(999 para parar):'))
    if n==999:
        break
    soma=soma+n
    q=q+1
print(f'Soma:{soma}')
print(f'Quantidade:{q}')