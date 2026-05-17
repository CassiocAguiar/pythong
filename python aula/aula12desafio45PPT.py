import random
ppt=('pedra','papel','tesoura')
escolha=input('digite pedra,papel ou tesoura para jogar contra a maquina:').lower()
maquina=random.choice(ppt)
if maquina==escolha:
    print('empate')
elif maquina=='tesoura' and escolha=='papel' or maquina=='pedra' and escolha=='tesoura' or maquina=='papel' and escolha=='pedra':
    print('maquina ganhou')
else:
    print('jogador ganhou')
