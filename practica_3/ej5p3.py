max = -999; min = 101
cond_clim = []
salir = False
while not salir:
    quedarse = raw_input("Ingrese 'si' para seguir o 'no' para salir: ")
    if quedarse == "si":
        temp = input("Ingrese temperatura: ")
        hum = input("Ingrese humedad: ")
        prob_lluv = input("Ingrece la probabilidad de lluvias: ")
        viento_vel = input("Ingrece la velocidad del viento: ")
        viento_dir = raw_input("Ingrese la direccion del viento: ")
        fecha = raw_input("Ingrese fecha: ")
        hora = raw_input("Ingrese hora: ")
        dat_almacenados = {"temp":temp, "hum":hum, "prob_lluv":prob_lluv, "viento_vel":viento_vel, "viento_dir":viento_dir, "fecha":fecha, "hora":hora}
	cond_clim.append(dat_almacenados)
    elif quedarse == "no":
        salir = True
print(cond_clim)
for dato in cond_clim:
    #print "Temperatura: " + str(dato["temp"])
    #print "Probabilidad de lluvias: " + str(dato["prob_lluv"])
    temp = dato["temp"]
    prob_lluv = dato["prob_lluv"]
    if temp > max:
        max = temp
        maxdato = dato
    if prob_lluv < min:
        min = prob_lluv
        mindato = dato
print "El dia %s con temperatura %s fue el mas caluroso" % (str(maxdato["fecha"]),str(max))
print "El dia %s fue el de menor probavilidad de lluvia, con un porcentaje de %s%%" % (mindato["fecha"],min)
