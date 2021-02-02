import random
score = 0
while True :
    n=random.randrange(0,9)
    m=random.randrange(0,9)
    som=n+m
    mos=int(input("donner la prédiction du somme : {}".format(som)))
    if mos == som :
        score+=1000
    else :
        print("mauvaise prédiction som = {}".format(som))
        print("votre score est {}".format(score))
        break
