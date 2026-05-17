import random
aluno1=input('digite o nome do seu aluno:')
aluno2=input('digite o nome do seu aluno:')
aluno3=input('digite o nome do seu aluno:')
aluno4=input('digite o nome do seu aluno:')
alunoal=(aluno1,aluno2,aluno3,aluno4)
escolhido=random.sample(alunoal,4)
print(f' a ordem para a apresentacao sera {escolhido}')
