teste = float(input('Introduza a nota do teste : '))
trab = float(input('Introduza a nota do trabalho : '))

media = teste*0.6 + trab*0.4

if (media>=9.5):
    print('A média é : ',media, ', o aluno está aprovado')
else:
    print('A média é : ',media, ', o aluno está reprovado')