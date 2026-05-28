d={}
d['nome']=input('digite o nome:')
ano=int(input('digite seu ano de nascimento:'))
d['idade']=2026-ano
d['ctps']=int(input('digite os pontos da CTPS(0 nao tem):'))
if d['ctps']!=0:
    d['contratacao']=int(input('digite o ano de contratacao:'))
    d['salario']=float(input('digite seu salario:'))
    quantof=35-(2026-d['contratacao'])
    d['aposentadoria']=d['idade']+quantof
for k,v in d.items():
    print(f'{k} tem o valor {v}')