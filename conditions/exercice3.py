a=int(input("donner l'entier a : "))
b=int(input("donner l'entier b : "))

if a == b :
    print("{} = {}".format(a,b))
elif a > b :
    print('{} > {}'.format(a,b))
else :
    print('{} < {}'.format(a,b))