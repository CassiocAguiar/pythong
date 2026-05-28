pessoas={'nome':'Cassio','sexo':'M','idade':18}
print(len(pessoas))
print(pessoas.items())
lista=[]
lista.append(pessoas)
print(lista[0]['nome'])
for k in pessoas.keys():
    print(k)
del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k}={v}')