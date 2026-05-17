ano=int(input('digite seu ano de nascimento:'))
categoria=2026-ano
if categoria<=9:
    print('Mirim')
elif categoria<=14:
    print('Infantil')
elif categoria<=19:
    print('Junior')
elif categoria<=20:
    print('Senior')
else:
    print('Master')