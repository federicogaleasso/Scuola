#GALEASSO FEDERICO 4C 23/11/2022 COMPITO - RETTANGOLO PROGRAMMAZIONE AD OGGETTI

#PROGETTARE SIA UML che CODICE PYTHON
#Creare una classe Rettangolo con attributi privati base ed altezza. Creare il metodo calcolaArea() che restituisce il valore dell'area del rettangolo. 
#Istanziare due oggetti rettangolo (usando o meno i parametri di default), calcolare l'area di entrambi e stabilire quale rettangolo ha l'area maggiore

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Rettangolo:
	def __init__(self, base=0, altezza=0, area=0):
		self.setBase(base)
		self.setAltezza(altezza)
		self.setArea(area)
		
	def setBase(self,base):
		self.__base=base

	def setAltezza(self,altezza):
		self.__altezza=altezza
		
	def setArea(self,area):
		self.__area=area

	def getBase(self):
		return self.__base

	def getAltezza(self):
		return self.__altezza

	def getArea(self):
		return self.__area

	def calcolaArea(self):
		print(f"\nL'area del rettangolo di base {self.getBase()} e altezza {self.getAltezza()} è: {self.getArea()}")

base=int(input("Inserisci la base del rettangolo: "))
altezza=int(input("Inserisci l'altezza del rettangolo: "))
area=base*altezza
rettangolo=Rettangolo(base,altezza,area)
rettangolo.calcolaArea()
