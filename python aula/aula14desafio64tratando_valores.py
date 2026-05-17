total=0
q=0
parar=0
while parar!=999:
    numero=int(input('digite um numero:'))
    total=total+numero
    q+=1
    parar=int(input('digite 999 para parar ou 1 para continuar:'))

    
print(f'foram digitados {q} numeros e a soma entre eles eh {total}')
