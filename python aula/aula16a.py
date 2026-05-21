lanche=('hamburguer','suco','pizza','pudim')
print(lanche[1:])
for cont in range(0,len(lanche)):
    print(f'vou comer {lanche[cont]}, posicao:{cont}')
for pos,comida in enumerate(lanche):
    print(f'vou comer {comida},posicao:{pos}')