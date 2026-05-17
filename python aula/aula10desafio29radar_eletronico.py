print('sabendo que o maximo de velocidade eh 80km, e acima disso implica uma multa de 7 reais por km acima do limite')
velocidade=float(input('digite a velocidade do carro:'))
if velocidade>80:
    print('voce foi multado')
    print(f'o preco a ser pago eh {(velocidade-80)*7} reais')
else:
    print('continue assim!')