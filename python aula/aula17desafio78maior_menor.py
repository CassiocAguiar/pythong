valores=[]
for c in range(0,5):
    valores.append(int(input('digite um numero:'))) 
print(f'menor valor:{min(valores)}, nas posicoes...', end='')
for p,minn in enumerate(valores):
    if minn==min(valores):
        print(p+1)
print(f'maior valor:{max(valores)},nas posicoes... ', end='')
for pm,mai in enumerate(valores):
    if mai==max(valores):
        print(pm+1) 