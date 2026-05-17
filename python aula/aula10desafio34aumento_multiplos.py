print('sabendo que salarios supeiores a 1.250 reais receberao um aumento de 10%, e para inferiores sera 15%')
salario=float(input('digite seu salario:'))
if salario>1250:
    print(f'seu salario foi de {salario:.2f} reais para {salario*1.10:.2f} reais')
else:
    print(f'seu salario foi de {salario:.2f} reais para {salario*1.15:.2f} reais')