ano=int(input('digite o ano do seu nascimento:'))
alistar=2026-ano
if alistar<18:
    print('voce ainda ira se alistar')
    print(f'falta {18-alistar} anos para voce se alistar')
elif alistar==18:
    print('hora de se alistar')
else:
    print('ja passou o tempo de alistamento')
    print(f'passou {alistar-18} anos do prazo de alistamento')
