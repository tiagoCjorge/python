print("Máximo e Mínimo")

notas=[]

contador=1

while contador<5:
    notas.append(float(input("Introduza a nota do teste")))
    contador += 1

maiornota=max(notas)
menornota=min(notas)
med=sum(notas)/len(notas)

print("A nota mais alta é ", maiornota)

print("A nota mais baixa é ", menornota)

print("A média das notas é ", med)
