persona=("Mariano","Rodriguez",34928850,1989,"La Plata",0)
nombre = persona[0]
apellido = persona[1]
DNI = persona[2]
ano_de_nacimiento = persona[3]
lugar_de_nacimiento = persona[4]
clave_personal = DNI*ano_de_nacimiento
pgp_casera = (clave_personal,"1234NNnn.:")
pgp_casera[1] = "12345NnN:." 

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

