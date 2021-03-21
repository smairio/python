quitter = 'F'
while quitter!='T' :
    while True :
        try :
            prixHT=float(input("Donner le prix hors tax :"))
            break
        except ValueError :
            print("Merci d'introduire un reel .")
    while True :
        try :
            TVA=int(input("pour le code 1 TVA=15% et pour le code 2 tva=19% ."))
            if TVA==1 :
                print(prixHT*(1+.15))
                break
            elif TVA==2 :
                print(prixHT*(1+.19))
                break
            except ValueError :
                print("SVP tappez 1 ou 2 .")