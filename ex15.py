a = int(input('Numero de alunos - '))

medT=0
negativasTeste=0
negativasTrab=0
posTrab=0
posTeste=0
for i in range (1,a+1):
    print('Aluno ',i)
    teste = float(input('Nota do teste - '))
    trab = float(input('Nota do Trabalho - '))
    medA=teste*0.5+trab*0.5
    if (teste<=9.5):
        negativasTeste += 1
    else:
        posTeste += 1
    if (trab<=9.5):
        negativasTrab += 1
    else:
        posTrab += 1
    medT+=medA

print('A média da turma é : ',medT/a)
print('Testes  - ',posTeste, 'Positivas e ',negativasTeste, 'Negativas')
print('Trabalhos - ',posTrab, 'Positivas e ', negativasTrab,'Negativas')