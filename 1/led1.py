import serial
import tkinter as tk
import cv2 
import time
import numpy as np
import matplotlib.pyplot as plt
#Serial objet, abrir la comunicacion
ard=serial.Serial("/dev/ttyUSB0",115200,timeout=1);
#c=input("Escriba un numero")
def binario(nn):
	bina=list(bin(nn))
	bina.pop(0)
	bina.pop(0)
	bin_int = [int(i) for i in bina]
	if len(bina)==1:
		bin_int.insert(0,0)
		bin_int.insert(0,0)
	if len(bina)==2:
		bin_int.insert(0,0)
	return(bin_int)
def apagado():
	ard.write(b'4');
	ard.write(b'5');
	ard.write(b'6');
	ard.write(b'7');
while (True):
	print("\n a: secuencia de numeros \n b: numeros en binario \n o: salir")
	c=input("Escriba la opcion")
	if (c=='a'):
		for i in range (0,8):
			arr = bytes(str(i), 'utf-8')
			ard.write(arr);
			#print(type(arr))
			time.sleep(1)
		print("Encender")
	'''#c=int(input("Escriba un numero"))'''
	if (c=='b'):
		lim=int(input("Ingrese el numero limite"))
		for decimal in range (0,lim):
			lista_bin=binario(decimal)
			print("binario",lista_bin)
			for bandera in range (0,len(lista_bin)):
				#print("La posicion es",bandera)
				if lista_bin[bandera]==1:
					arr= bytes(str(bandera), 'utf-8')
					ard.write(arr);
					#print(bandera)
				else:
					aux=bandera+4
					#print(aux)
					arr= bytes(str(aux), 'utf-8')
					ard.write(arr);
			time.sleep(2)
			apagado()
	if(c=='o'):
		print("Cerrar")
		break
