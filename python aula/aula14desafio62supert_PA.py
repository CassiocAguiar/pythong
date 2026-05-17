primeiro=int(input('digite o primeiro termo da pa:'))
razao=int(input('digite a razao da pa:'))
termo=primeiro
t=0
total=0
mais=10
while mais!=0:
    total=total+mais
    while t!=total:
        print(termo,end='-')
        t+=1
        termo=termo+razao
    print('PAUSA')
    mais=int(input('voce quer que a pa ultrapasse 10 termos?digite a quantidade de termos a mais,se nao digite 0 para parar:'))
print('FIM')
    