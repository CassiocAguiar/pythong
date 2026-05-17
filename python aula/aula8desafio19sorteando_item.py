from random import choice
aluno1=input('digite o nome do seu aluno:')
aluno2=input('digite o nome do seu aluno:')
aluno3=input('digite o nome do seu aluno:')
aluno4=input('digite o nome do seu aluno:')
alunoal=(aluno1,aluno2,aluno3,aluno4)
escolhido=choice(alunoal)
print(f'o aluno escolhido para limpar o quadro foi o {escolhido}')
