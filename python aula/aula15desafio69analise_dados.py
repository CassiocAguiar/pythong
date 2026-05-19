m=0
h=0
mn=0
pc=0
while True:
    idade=int(input('digite sua idade:'))
    sexo=str(input('digite seu sexo[M/F]:')).upper().strip()[0]
    while sexo!='M' and sexo!='F':
        print('Opcao invalida')
        sexo=str(input('digite um sexo valido[M/F]:')).upper().strip()[0]
    pc=pc+1
    if idade >= 18:
        m += 1   
    # Quantos homens foram cadastrados?
    if sexo == 'M':
        h += 1   
    # Quantas mulheres têm menos de 20 anos?
    if sexo == 'F' and idade < 20:
        mn += 1
    escolha=int(input('deseja parar?digite 0,para continuar digite 1:'))
    while escolha!=0 and escolha!=1:
        print('Invalido')
        escolha=int(input('Por favor,digite 0 para parar ou 1 para continuar:'))
    if escolha==0:
        print('Finalizando...')
        break
print(f'numero de pessoas acima de 18 anos:{m}')
print(f'numero de homens cadastrados:{h}')
print(f'numero de mulheres abaixo de 20 anos:{mn}')
print(f'numero de pessoas cadastradas:{pc}')
