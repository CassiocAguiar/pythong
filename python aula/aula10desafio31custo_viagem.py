print('sabemos que viagens de ate 200km o preco a ser pago eh 0.50 por km,acima disso 0.45')
distancia=float(input('digite a distancia da sua viagem em km:'))
if distancia<=200:
    print(f'o valor a ser pago eh {distancia*0.50} reais')
else:
    print(f'o valor a ser pago eh {distancia*0.45}')