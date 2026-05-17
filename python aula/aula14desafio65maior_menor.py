maior=0
menor=0
total=0
m=0
parar=1
while parar!=0:
    numero=int(input('digite um valor:'))
    total=total+numero
    if m==0:
        maior=numero
        menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero 
    m=m+1
    parar=int(input('digite 1 para continuar,digite 0 para parar:'))
media=total/m
print(f'a media dos valores eh:{media}')
print(f'o maior numero eh {maior}')
print(f'o menor numero foi {menor}')
      