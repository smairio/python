nc1 = float(input("donner le note de control 1 : "))
nc2 = float(input("donner le note do control 2 : "))

moy= (nc1+nc2)/2
print("votre moyen {}".format(moy))
if moy >= 10 :
    print("Félicitations ! Vous avez validé cette matiere.")
else :
    print("N'est pas validé")