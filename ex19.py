p = input('Escreva uma palavra - ')
v=0
p = p.lower()

vogais = ['a','e','i','o','u']

for i in range (0,len(p)):
    for j in range(0,len(vogais)):
        if (p[i] == vogais[j]):
            v += 1

print(v)
