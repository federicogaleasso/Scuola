#GALEASSO FEDERICO 4C 23/11/2022 COMPITO - PUNTO PROGRAMMAZIONE AD OGGETTI

#PROGETTARE SIA UML che CODICE PYTHON
#Creare una classe Punto con attributi privati x e y. Creare il metodo calcolaDistanza() che restituisce il valore della distanza del punto dall'origine degli assi. 
#Istanziare due oggetti punto (usando o meno i parametri di default), calcolare e stampare la distanza tra i due punti.

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Punto:
	def __init__(self, x=0, y=0, distanza=0):
		self.setX(x)
		self.setY(y)
		self.setDistanza(distanza)
		
	def setX(self,x):
		self.__x=x

	def setY(self,altezza):
		self.__y=y
		
	def setDistanza(self,area):
		self.__distanza=distanza

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def getDistanza(self):
		return self.__distanza

	def calcolaDistanza(self):
		print(f"\nLa distanza tra il punto X ({self.getX()}) e il punto Y ({self.getY()}) è: {self.getDistanza()}")

x=int(input("Inserisci il punto X: "))
y=int(input("Inserisci il punto Y: "))
distanza=x-y
punto=Punto(x,y,distanza)
punto.calcolaDistanza()
