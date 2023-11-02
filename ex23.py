print("Contador Elementos Iguais em Listas")

lista1=[]
lista2=[]

contador=1
contador2=1

ci= 0

while contador<5:
    lista1.append(float(input("Introduza numeros da 1ª lista: ")))
    contador += 1

while contador2<5:
    lista2.append(float(input("Introduza numeros da 2ª lista: ")))
    contador2 += 1

for i in lista1:
    for j in lista2:
        if i == j :
            ci += 1




print("Entre as duas listas existem ", ci," elementos iguais.")
