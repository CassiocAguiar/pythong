cin=0
vin=0
dez=0
um=0
while True:
    valor=int(input('digite o valor a ser sacado:'))
    if valor==0:
        print('Finalizando...')
        break
    if valor>=50:
        cin=valor//50
        valor=valor%50
    if valor>=20:
        vin=valor//20
        valor=valor%20
    if valor>=10:
        dez=valor//10
        valor=valor%10
    if valor>=1:
        um=valor//1
        valor=valor%1
    break
print('-'*30)
print(f'total de cedulas de 50:{cin}')
print(f'total de cedulas de 20:{vin}')
print(f'total de cedulas de 10:{dez}')
print(f'total de cedulas de 1:{um}')
print('-'*30)
