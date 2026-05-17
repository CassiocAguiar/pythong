import random
numero=int(input('escolha entre um numero de 0 a 10 que voce acha que a maquina escolheu:'))
nescolhido=random.randint(0,10)
t=0
while numero!=nescolhido:
    numero=int(input('voce errou tente outro numero:'))
    t=t+1
print(f'voce acertou!numero de tentativas: {t} vezes')