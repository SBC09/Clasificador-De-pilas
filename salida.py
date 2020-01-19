from salida2 import correcto
from salida2 import incorrecto
def output():
 fiaudio = open("Pilas.txt", "r")
 string1=fiaudio.read()
# abrir el ficheros de salidaclasificacion
 fiaudio.close()
fimedidas=open("salidaclasificacion.txt","r")
string2=fimedidas.read()
fimedidas.close()


if string1==string2:

    correcto()
else:
    incorrecto()

