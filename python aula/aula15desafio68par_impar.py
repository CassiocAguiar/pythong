import random
maquina=''
v=0
soma=0
jogador=0
vm=0
while True:
    print('[1] para ser par')
    print('[2] para ser impar')
    escolhaj=int(input('escolha:'))
    jogador=int(input('digite um numero de 0 a 10:'))
    maquina=random.randint(0,10)
    soma=jogador+maquina
    print(f'numero escolhido pelo jogador:{jogador}')
    print(f'numero escolhido pela maquina:{maquina}')
    print(f'a soma:{soma}')
    if escolhaj==1:
        if soma%2==0:
            print('Jogador venceu')
            v=v+1
        else:
            print('Jogador perdeu')
            vm=vm+1
            break
    elif escolhaj==2:
        if soma%2!=0:
            print('Jogador venceu')
            v=v+1
        else:
            print('Jogador perdeu')
            vm=vm+1
            break
print(f'numero de vitorias do jogador:{v}')
print(f'numero de vitorias da maquina:{vm}')
