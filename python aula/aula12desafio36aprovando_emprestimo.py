vcasa=float(input('digite o valor da casa:'))
salario=float(input('digite o valor do seu salario:'))
anos=int(input('digite em quantos anos voce ira pagar a casa:'))
pmensal=(vcasa/anos)/12
if pmensal>salario*0.3:
    print('emprestimo negado')
else:
    print('emprestimo concedido')