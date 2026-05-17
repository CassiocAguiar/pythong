numero=int(input('digite um numero inteiro:'))
hexa=hex(numero)
binario=bin(numero)
octal=oct(numero)

print(f'hexadecimal: {hexa[2:]}')
print(f'binario: {binario[2:]}')
print(f'octal: {octal[2:]}')