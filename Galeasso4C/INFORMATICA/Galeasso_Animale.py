#GALEASSO FEDERICO 4C 15/12/2022 ESERCIZIO IN CLASSE - ANIMALE OOP

#Progettazione classe Animale in Py
#Creare (UML e Python) una classe Animale con metodi di setNome, getNome, setPeso, getPeso, setSesso, getSesso, verso, interroga (che restituisce il tipo di animale).
#Creare 4 oggetti di tipo animale (cane, gatto, ippopotamo,...), fare in modo che si presentino e facciano il loro verso, settare il peso ed il sesso.

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Animale:
	def __init__(self, nome="", peso=0.0, sesso="", verso=""):
		self.setNome(nome)
		self.setPeso(peso)
		self.setSesso(sesso)
		self.setVerso(verso)
		
	def setNome(self,nome):
		self.__nome=nome

	def setPeso(self,peso):
		self.__peso=peso
		
	def setSesso(self,sesso):
		self.__sesso=sesso
		
	def setVerso(self,verso):
		self.__verso=verso

	def getNome(self):
		return self.__nome

	def getPeso(self):
		return self.__peso

	def getSesso(self):
		return self.__sesso
		
	def getVerso(self):
		return self.__verso

	def interroga(self):
		print(f"\nAnimale: {self.getNome()} | Peso: {self.getPeso()} | Sesso: {self.getSesso()} | Verso: {self.getVerso()}")

for i in range(4):
	nome=input("Inserisci il nome dell'animale: ")
	peso=float(input("Inserisci il peso dell'animale: "))
	sesso=input("Inserisci il sesso dell'animale: ")
	verso=input("Inserisci il verso dell'animale: ")
	animale=Animale(nome,peso,sesso,verso)
	animale.interroga()
