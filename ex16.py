i=1
par = 0
impar = 0
while i!=0:
    i = int(input('Introduza um numero (0 para sair) - '))
    if (i==0):
        break
    if (i%2==0 ):
        par += 1 
    else:
        impar += 1

print(par, ' numeros pares')
print(impar, ' numeros impares')