frase=str(input('digite um frase:')).upper().strip()
frasea=frase.count('A')
frase1=frase.find('A')+1
fraseu=frase.rfind('A')+1
print(f'numero de vezes que a aparece a letra A eh: {frasea} , primeira vez que aparece {frase1} e a ultima vez que aparece {fraseu}')