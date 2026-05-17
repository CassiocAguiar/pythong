import math
angulo=float(input('digite o valor do angulo em graus:'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f'o angulo de {angulo} graus tem valor de seno {seno:.2f} de cosseno {cosseno:.2f} e de tangente {tangente:.2f}')