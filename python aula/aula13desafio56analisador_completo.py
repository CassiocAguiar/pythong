idade = 0
idm = 0

for p in range(1, 5):
    ano = int(input(f'data de nascimento da {p} pessoa: '))
    nome = input(f'nome da {p} pessoa: ')
    sexo = input(f'sexo da {p} pessoa, digite M ou F: ').upper()
    idade_pessoa = 2026 - ano
    idade += idade_pessoa
    # homem mais velho
    if sexo == 'M':
        if p == 1:
            menor = ano
            nome_velho = nome
        elif ano < menor:
            menor = ano
            nome_velho = nome
    # mulheres com menos de 20
    if sexo == 'F' and idade_pessoa < 20:
        idm += 1
media = idade / 4
print(f'a media de idade do grupo eh {media}')
print(f'o homem mais velho eh {nome_velho}')
print(f'a quantidade de mulheres com menos de 20 anos eh {idm}')