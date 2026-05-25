lista = (str(input('Digite a expressão: '))).replace('', ' ').split()
if lista.count('(') == lista.count(')') and lista.index('(') < lista.index(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')