carac = raw_input("Ingrese una letra: ")
vocales = "AaEeIiOoUu"
consonantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghijklmnpqrstuxyz"
def letra(carac, vocales, consonantes):
    for i in vocales:
        if i == carac:
            return 1
    for i in consonantes:
        if i == carac:
            return 2
if letra(carac, vocales, consonantes) == 1:
    print("%s es vocal!" %(carac))
if letra(carac, vocales, consonantes) == 2:
    print("%s es consonante!" %(carac))
