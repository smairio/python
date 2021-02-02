import random
print("generer un nombre entre 1 et 10")
x=random.randrange(1,10)
print("done.")
y=int(input("prédire le nombre "))

if x == y :
    print("bravo!")
elif x==y+1 or x==y-1:
    print('deuxième et dernière chance')
    x=int(input("prédire le nombre"))
    if x==y :
        print("bravo!")
    else :
        print("Echec nombre = {}".format(x))
else :
    print("Echec nombre = {}".format(x))