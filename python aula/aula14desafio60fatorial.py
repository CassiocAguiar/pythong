"""import math
n1=int(input('digite um numero:'))
t=0
while t!=1:
    print(math.factorial(n1))
    t+=1"""

"""numero = int(input("Fatorial de: "))
resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1
print(f"{numero}! = {resultado}")"""

numero = int(input("Fatorial de: "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print(f"{numero}! = {resultado}")
