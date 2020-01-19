import MySQLdb
import numpy as np
from StringIO import StringIO
def clasificacion():
  error=5
  dirFichero='/BSS/SENSORS/medidas.txt'
  f=open(dirFichero,'r')
  datos=f.read()
  f.close()
  datos=np.genfromtxt(StringIO(datos))
  
  db=MySQLdb.connect(
  		host="localhost",
  		user="root",
  		passwd="1234",
  		db="STR")
  cursor=db.cursor()
  sql="SELECT * FROM pilas WHERE DIAMETRO <=%s AND DIAMETRO >=%s AND ALTURA <=%s AND ALTURA>=%s AND PESO <=%s AND PESO >=%s"
  diaM=datos[0]+(datos[0]/error)
  diam=datos[0]-(datos[0]/error)
  altM=datos[1]+(datos[1]/error)
  altm=datos[1]-(datos[1]/error)
  pesM=datos[2]+(datos[2]/error)
  pesm=datos[2]-(datos[2]/error)
  
  cursor.execute(sql,(diaM,diam,altM,altm,pesM,pesm))
  e=open("salidaclasificacion.txt","w")
  for row in cursor.fetchall():
  	e.write(row[1]+'\n')
  cursor.close()
  db.close()
  e.close()
