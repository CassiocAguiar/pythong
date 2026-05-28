d={}
for c in range(0,2):
    d['nome']=input('digite o nome do aluno:')
    d['media']=float(input('digite a media do aluno:'))
    if d['media']>=7:
        d['situacao']='boa'
    else:
        d['situacao']='ruim'
    break
for k,v in d.items():
    print(f'o {k} eh igual a {v}')

