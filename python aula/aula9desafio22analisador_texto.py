nome=input('digite seu nome:')
nomeseparado=nome.split()
nomesemespaco=''.join(nomeseparado)
primeironome=nomeseparado[0]
print(f'seu nome com todas as letras maisculas fica assim {nome.upper()} e com todas minusculas fica assim {nome.lower()}')
print(f'seu nome tem {len(nomesemespaco)} letras')
print(f'seu primeiro nome tem {len(primeironome)} letras')