#!/usr/bin/python


import sys
import mraa
import time
def medida_de_pilas():
    #Use pin 7 by default
    pin_no1=15
    pin_no2=13
    # Export the GPIO pin for use
    pin1 = mraa.Gpio(pin_no1)
    pin2 = mraa.Gpio(pin_no2)
    
    # Small delay to allow udev rules to execute (necessary only on up)
    time.sleep(0.1)
    
    # Configure the pin direction
    pin1.dir(mraa.DIR_OUT)
    pin2.dir(mraa.DIR_OUT)
    
        # Turn the LED on and wait for 0.5 seconds
    pin1.write(1)
    time.sleep(0.01)
    pin1.write(0)
        # Turn the LED off and wait for 0.5 seconds
    pin1.dir(mraa.DIR_IN)
    
    while True:
      pulso_inicio1 = time.time()
      pulso1 = pin1.read()
      if pulso1:
       break
    
    while True:
      pulso_fin1 = time.time()
      pulso1 = pin1.read()
      if not pulso1:
       break
    
    duracion1 = pulso_fin1 - pulso_inicio1
    
    distancia1 = (34300 * duracion1) / 2
    
    print ("Distacia Ancho: %.2f cm" % distancia1)
    
    pin2.write(1)
    time.sleep(0.01)
    pin2.write(0)
    pin2.dir(mraa.DIR_IN)
    
    while True:
      pulso_inicio2 = time.time()
      pulso2 = pin2.read()
      if pulso2:
       break
    
    while True:
      pulso_fin2 = time.time()
      pulso2 = pin2.read()
      if not pulso2:
       break
    
    duracion2 = pulso_fin2 - pulso_inicio2
    distancia2 = (34300 * duracion2) / 2
    
    print ("Distancia Largo: %.2f cm" %distancia2)
    e=open("medidas.txt","w")
    e.write(str(round(distancia1, 2))+'\n')
    e.write(str(round(distancia2, 2))+'\n')
    e.close()
    
    pin1.dir(mraa.DIR_OUT)
    pin2.dir(mraa.DIR_OUT)
    fichero
