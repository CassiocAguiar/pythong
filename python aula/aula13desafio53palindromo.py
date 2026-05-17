'''frase=input('digite uma frase para saber se ela eh um palindromo:').replace(' ','').lower()
if frase==frase[::-1]:
    print(f'o inverso da {frase} eh {frase[::-1]}')
    print('TEMOS UM PALINDROMO')
else:
    print(f'o inverso da {frase} eh {frase[::-1]}')
    print('NAO TEMOS UM PALINDROMO')'''
frase=input('digite uma frase: ').replace(' ','').lower()

inverso=''

for letra in range(len(frase)-1,-1,-1):
    inverso += frase[letra]

print(inverso)

if frase == inverso:
    print('TEMOS UM PALINDROMO')
else:
    print('NAO TEMOS UM PALINDROMO')