total=0
m=0
menor=0
nomem=''
while True:
    produto=str(input('digite o nome do produto:'))
    preco=float(input('digite o preco do produto: R$'))
    if total==0:
        menor=preco
        nomem=produto
    elif preco<menor:
        menor=preco
        nomem=produto
    if preco>1000:
        m=m+1
    total=total+preco
    escolha=str(input('digite C para continuar,digite P para parar:')).upper()
    while escolha!='C' and escolha!='P':
        print('Invalido')
        escolha=str(input('digite C ou P:')).upper()
    if escolha=='P':
        print('Finalizando...')
        break
print(f'total gasto:{total}')
print(f'produtos que custam mais de 1000 reais:{m}')
print(f'nome do produto mais barato:{nomem},seu preco:{menor}')