n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))
def max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return 0
    if n1 > n2 and n1 < n3:
        return 1
    if n1 < n2 and n1 > n3:
        return 2
if max_de_tres(n1,n2,n3) == 0:
    print("El numero mayor es %s (if1)" % (n1))
if max_de_tres(n1,n2,n3) == 1:
    print("El numero mayor es %s (if2)" % (n3))
if max_de_tres(n1,n2,n3) == 2:
    print("El numero mayor es %s (if3)" % (n2))
