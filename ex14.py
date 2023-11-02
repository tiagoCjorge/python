a = int(input('Numero de alunos - '))

medT=0


for i in range (1,a+1):
    print('Aluno ',i)
    teste = float(input('Nota do teste - '))
    trab = float(input('Nota do Trabalho - '))
    medA=teste*0.5+trab*0.5
    medT+=medA

print('A média da turma é : ',medT/a)