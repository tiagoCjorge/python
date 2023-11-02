from random import randrange
import random 


n = random.randrange(1,100)

i=0
t=0

while (i<4 and t!=n):
    t = int(input('Tente adivinhar o numero entre 1 e 100 - ' ))
    if (t==n):
        print('Palpite correto!!!')
        break
    else:
        i+=1
    if i==3:
        print('Gastou as 3 tentativas, o numero era ',n)


