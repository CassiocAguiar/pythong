sexo='M'
while sexo!='M' and sexo!='F':
    sexo=str(input('Por favor,informe seu sexo[M/F]:')).upper()
    if sexo!='M' and sexo!='F':
        sexo=input('Informe uma resposta valida:').upper()
