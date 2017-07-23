comandos = []
salir = False
while not salir:
	palabras = raw_input("ingrese palabra: ")
	if palabras != "0000":
		comandos.append(palabras)
		print("Palabra guardada, para salir ingrese 0000")
	elif palabras == "0000":
		print("Fianlizo el programa")
		salir = True
print(comandos)
