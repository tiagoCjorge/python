p = input('Escreva uma palavra - ')
v=0
c=0
p = p.lower()

vogais = ['a','e','i','o','u']
for i in p:
        if i.isalpha():
            if i in vogais : 
                 v+=1
            else:
              c+=1

print('Vogais : ',v,' | Consuantes : ',c)
