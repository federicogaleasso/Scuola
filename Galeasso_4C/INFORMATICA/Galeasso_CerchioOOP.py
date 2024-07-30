#GALEASSO FEDERICO 4C 12/12/2022 APPUNTI CPOMMENTATI OOP

#Scrivete una definizione di classe di nome Cerchio , avente gli attributi centro e raggio , dove centro è un oggetto Punto e raggio è un numero. Istanziate un oggetto Cerchio che rappresenti un cerchio con il centro nel punto ( 150, 100 ) e di raggio 75.
#Scrivete una funzione di nome punto_nel_cerchio, che prenda un Cerchio e un Punto e restituisca True se il punto giace dentro il cerchio, circonferenza compresa.
#Scrivete una funzione di nome rett_nel_cerchio, che prenda un Cerchio e un Rettangolo e restituisca True se il rettangolo giace interamente all’interno del cerchio, circonferenza compresa.
#Scrivete una funzione di nome rett_cerchio_sovrapp, che prenda un Cerchio e un Rettangolo e restituisca True se almeno uno degli angoli del Rettangolo ricade all’interno del cerchio.

import os
import copy

def clearScreen():
	os.system("clear")
clearScreen()

class Cerchio():
	def __init__(self, raggio=0, objcentro=0):
		self.setRaggio(raggio)
		self.setobjCentro(objcentro)
		
	def setRaggio(self,raggio):
		self.__raggio=raggio

	def setobjCentro(self,objcentro):
		self.__objcentro=objcentro

	def getRaggio(self):
		return self.__raggio

	def getobjCentro(self):
		return self.__objcentro
		
	def __str__(self):
		return "Centro: "+str(self.getRaggio())+"\nRaggio: "+str(self.getobjCentro())
		
class Punto():
	def __init__(self,valx=0,valy=0):
		self.set_x(valx)
		self.set_y(valy)

	def __str__(self):
		return "("+str(self.get_x())+","+str(self.get_y())+")"

	def set_x(self,vx):
		self.__x=vx

	def get_x(self):
		return self.__x

	def set_y(self,vy):
		self.__y=vy

	def get_y(self):
		return self.__y

nuovoPunto=Punto(150,100)

nuovoCerchio=Cerchio(nuovoPunto,75)
print(nuovoCerchio)

def punto_nel_cerchio():	#Un punto appartiene al cerchio se la distanza dal centro è minore o uguale al raggio.
	punto1=Punto(80,120)
	cerchio1=Cerchio(punto1,50)
	print(cerchio1)
	if punto1<=50:
		print("True\n")
	else:
		print("False\n")

def rett_nel_cerchio():
	punto2=Punto(50,220)
	cerchio2=Cerchio(punto1,80)
	areaCerchio=(80**2)*3.14
	base=int(input("Inserisci la base del rettangolo: "))
	altezza=int(input("Inserisci l'altezza del rettangolo: "))
	areaRettangolo=base*altezza
	if areaCerchio > areaRettangolo:
		print("True\n")
	else:
		print("False\n")
		
rett_nel_cerchio()
punto_nel_cerchio()
