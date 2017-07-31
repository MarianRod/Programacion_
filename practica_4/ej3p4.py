cant = 0
cant2 = 0
cadena = "Esto es una cadena"
lista = ["0","1","2","3","4","5","6","7","8"]
def medir(cant,cant2,cadena,lista):
    for i in cadena:
        if i == i:
            cant2 = cant2 + 1
    for i in lista:
        if i == i:
            cant = cant + 1
    return cant2,cant
dato = medir(cant,cant2,cadena,lista)
print(medir(cant,cadena,lista))
