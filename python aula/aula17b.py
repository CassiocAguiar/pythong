valores=[]
for cont in range(0,5):
    valores.append(int(input('digite um numero:')))
#print('valores da lista sao:',end='')
#for v in valores:
    #print(v,end=' ')
for c,v in enumerate(valores):
    print(f'na posica {c+1} encontrei {v}...')