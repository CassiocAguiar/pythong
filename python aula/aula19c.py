estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=input('digite o estado:')
    estado['sigla']=input('digite a sigla:')
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(k,  v)