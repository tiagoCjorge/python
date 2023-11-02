from random import randrange
lista = []
spar = 0
simp = 0
for i in range(20):
    lista.append(randrange(1,100))
    if (lista[i]%2==0):
        spar+=lista[i]
    else:
        simp+=lista[i]
        

print(lista)
print('Soma dos pares = ',spar)
print('Soma dos impares = ',simp)