produto=float(input('digite o valor do produto:'))
metodo=int(input('digite 1 se for pagar a vista, digite 2 se for a vista no cartao,digite 3 se for ate 2x no cartao,digite 4 se for 3x ou mais no cartao:'))
if metodo==1:
    print(f'voce recebeu um desconto de 10% por pagar a vista, o preco do produto ficou:{produto*0.9} reais')
elif metodo==2:
    print(f'voce recebeu um desconto de 5% por pagar a vista no cartao, o preco do produto ficou:{produto*0.95} reais')
elif metodo==3:
    print(f'voce ira pagar ate em 2x no cartao o preco do produto nao se altera:{produto} reais')
else:
    print(f'voce ira pagar em 3x ou mais no cartao,ocasionando em 20% de juros, o preco do produto ficou:{produto*1.20} reais')