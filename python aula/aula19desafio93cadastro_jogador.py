d={}
golp={}
listagolp=[]
q=0
dicionario={}
nome=input('digite o nome do jogador:')
partidas=int(input('digite a quantidade de partidas jogadas:'))
for c in range(1,partidas+1):
    golp[f'{c} partida,gols']=int(input(f'{c} partida fez quantos gols?:'))
    q=q+golp[f'{c} partida,gols']
listagolp.append(golp.copy())
dicionario['nome']=nome
dicionario['total de partidas']=partidas
dicionario['total de gols']=q
dicionario['gols por partida']=listagolp
print(dicionario)
for k,v in dicionario.items():
    print(k, v)