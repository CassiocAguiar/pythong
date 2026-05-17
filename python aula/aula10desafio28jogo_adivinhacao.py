import random
numeroal= 0,1,2,3,4,5
nescolhido=random.choice(numeroal)
adivinhacao=int(input('digite qual numero voce acha que a maquina escolheu:'))
if nescolhido==adivinhacao:
    print('parabens voce acertou')
else:
    print('voce errou')
print(f'numero escolhido pela maquina foi {nescolhido}')