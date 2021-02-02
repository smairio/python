argent=int(input("donner le somme d'argent: "))
while argent > 0 :
    n=int(input("donner une depense: "))
    argent-=n
if argent == 0 :
        print("argent est termineée")
else :
        print("vous avez atient le limite avec {}".format(-argent))