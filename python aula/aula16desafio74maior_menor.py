import random
menor=0
maior=0
m=0
print('Valores Sorteados')
for c in range(0,5):
    sorteio=random.randint(1,999)
    print(sorteio,end='-')
    if m==0:
        menor=sorteio
    elif sorteio<menor:
        menor=sorteio
    if m==0:
        maior=sorteio
    elif sorteio>maior:
        maior=sorteio
    m=m+1
    
print(f'menor numero:{menor}')
print(f'maior numero:{maior}')