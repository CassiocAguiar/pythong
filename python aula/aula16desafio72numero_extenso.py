numero=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n=int(input('digite um numero entre 0 a 20:'))
    while n<0 or n>20:
        n=int(input('entre 0 a 20 apenas:'))
    if n>=0 and n<=20:
        break
print(f'voce digitou:{numero[n]}')