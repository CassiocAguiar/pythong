from random import randint
from time import sleep
from operator import itemgetter
dados={'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
ranking=[]
print('Valores Sorteados')
for k,v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking=sorted(dados.items(),reverse=True,key=itemgetter(1))
for i,v in enumerate(ranking):
    print(f'{i+1} colocado:{v[0]} total de pontos:{v[1]}')