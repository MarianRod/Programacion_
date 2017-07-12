dic = {}
palabras = ["palabra1","palabra2","palabra2","palabra","palabra1","palabra3"]
for pal in palabras:
    #print(str(pal))
    c = 0
    for pal2 in palabras:
        if pal == pal2:
            c = c+1
    dic[pal] = c
print(palabras)
print(dic)
