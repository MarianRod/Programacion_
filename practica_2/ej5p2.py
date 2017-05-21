n = input("ingrese un ano: ")
if (n%4==0):
    if (n%100==0):
        if (n%400==0):
            print "el ano es bisiesto1"
        else:
            print "el ano no es bisiesto2"
    else:
        print "el ano es bisiesto3"
else:
    print "el ano no es bisiesto4"
