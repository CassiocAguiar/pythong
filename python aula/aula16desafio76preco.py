produto=('lapis',1.75,'caneta',2,'caderno',19.50,'apontador',4)
for pos in range(0,len(produto)):
    if pos%2==0:
        print(f'{produto[pos]}:',end='')
    else:
        print(f'R${produto[pos]:.2f}')