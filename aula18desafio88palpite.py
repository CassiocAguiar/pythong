from random import sample
import time
q=int(input('digite a quantidade de jogos para ser sorteado:'))
print(f'Sorteando {q} jogos')
for c in range(1,q+1):
    n=sample(range(1,60),6)
    print(n)
    time.sleep(0.8)