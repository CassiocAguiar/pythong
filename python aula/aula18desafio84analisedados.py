pessoas = []
dados = []
maior = 0
menor = 0

while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite o peso dela: '))
    
    dados.append(nome)
    dados.append(peso)
    
    if len(pessoas) == 0:
        menor = dados[1]
        maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
            
    pessoas.append(dados[:])
    dados.clear()
    
    c = input('Digite C para continuar ou P para parar [P/C]: ').upper().strip()[0]
    
    while c != 'P' and c != 'C':
        c = input('Apenas P ou C: ').upper().strip()[0]
        
    if c == 'P':
        break

print('-' * 30)
print(f'Número de pessoas cadastradas: {len(pessoas)}')

print(f'Maior peso: {maior}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()  # Quebra de linha

print(f'Menor peso: {menor}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()  # Quebra de linha