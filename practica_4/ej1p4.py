n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
def max_num (n1,n2):
    if n1 > n2:
       return 0
    if n1 < n2:
        return 1
    if n1 == n2:
        return 2
if max_num(n1,n2) == 0:
    print("El numero %s es mayor a %s" % (n1, n2))
if max_num(n1,n2) == 1:
    print("El numero %s es menor a %s" % (n1,n2))
if max_num(n1,n2) == 2:
    print("Los numeros son iguales")
