n=0
palavras=('macaco','abelha','urso','hipopotamo')
for p in palavras:
    print(f'\nna palavra {p} temos ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end=' ')
    