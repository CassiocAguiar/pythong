brasileirao = (
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "São Paulo",
    "Athletico-PR",
    "RB Bragantino",
    "Coritiba",
    "Bahia",
    "Vitória",
    "Botafogo",
    "Atlético-MG",
    "Internacional",
    "Vasco da Gama",
    "Grêmio",
    "Cruzeiro",
    "Corinthians",
    "Santos",
    "Mirassol",
    "Remo",
    "Chapecoense"
)
print('5 PRIMEIROS')
for c in range(0,5):
    print(brasileirao[c])
print('4 ULTIMOS COLOCADOS')
for cont in range(16,20):
    print(brasileirao[cont])
print('ORDEM ALFABETICA')
print(f'ordem alfabetica:{sorted(brasileirao)}')
print('POSICAO CHAPE')
print(f'posicao da chapecoense:{brasileirao.index("Chapecoense")+1}')