#GALEASSO FEDERICO 4C 22/1/2023 COMPITO PALESTRA OOP

import os
def clearScreen():
	os.system("clear")
clearScreen()

# classe Disciplina()
class Disciplina():
	def __init__(self, Nome='', CostoMensile=0):
		self.set_Nome(Nome)
		self.set_CostoMensile(CostoMensile)
		  
	def set_Nome(self, Nome):
		self.__Nome = Nome
		
	def get_Nome(self):
		return self.__Nome
		
	def set_CostoMensile(self, CostoMensile):
		self.__CostoMensile = CostoMensile
		
	def get_CostoMensile(self):
		return self.__CostoMensile
		
	def __str__(self):
		return f'Nome: {self.__Nome} | Costo mensile: {self.__CostoMensile}'

# classe Nuoto(Disciplina)
class Nuoto(Disciplina):
	def __init__(self, Nome='', CostoMensile=0, listaIscritti=[]):
		super().__init__(Nome, CostoMensile)
		self.set_listaIscritti(listaIscritti)
		
	def set_listaIscritti(self, listaIscritti):
		self.__listaIscritti = listaIscritti
		
	def get_listaIscritti(self):
		return self.__listaIscritti
		
	def __str__(self):
		return f'{super().__str__()} | Lista iscritti: {self.__listaIscritti}'

# classe Aerobica(Disciplina)
class Aerobica(Disciplina):
	def __init__(self, Nome='', CostoMensile=0, listaIscritti=[]):
		super().__init__(Nome, CostoMensile)
		self.set_listaIscritti(listaIscritti)
		
	def set_listaIscritti(self, listaIscritti):
		self.__listaIscritti = listaIscritti
		
	def get_listaIscritti(self):
		return self.__listaIscritti
		
	def __str__(self):
		return f'{super().__str__()} | Lista iscritti: {self.__listaIscritti}'

# classe Bodybuilding(Disciplina)
class Bodybuilding(Disciplina):
	def __init__(self, Nome='', CostoMensile=0, listaIscritti=[]):
		super().__init__(Nome, CostoMensile)
		self.set_listaIscritti(listaIscritti)
		
	def set_listaIscritti(self, listaIscritti):
		self.__listaIscritti = listaIscritti
		
	def get_listaIscritti(self):
		return self.__listaIscritti
		
	def __str__(self):
		return f'{super().__str__()} | Lista iscritti: {self.__listaIscritti}'
		
# classe Iscritto()
class Iscritto():
	def __init__(self, Nome='', Cognome=0, listaCorsi=[]):
		self.set_Nome(Nome)
		self.set_Cognome(Cognome)
		self.listaCorsi=[]
		  
	def set_Nome(self, Nome):
		self.__Nome = Nome
		
	def get_Nome(self):
		return self.__Nome
		
	def set_Cognome(self, Cognome):
		self.__Cognome = Cognome
		
	def get_Cognome(self):
		return self.__Cognome
		
	def addCorsi(self, disciplina):
		self.listaCorsi.append(disciplina)
		
	def get_listaCorsi(self):
		return self.__listaCorsi
		
	def __str__(self):
		return f'Nome: {self.__Nome} | Cognome: {self.__Cognome} | Lista corsi: {self.__listaCorsi}'
		
# classe Circolo()
class Circolo():
	def __init__(self, Nome='', listaIscritti=[]):
		self.set_Nome(Nome)
		self.listaIscritti=[]
	
	def set_Nome(self, Nome):
		self.__Nome = Nome
		
	def get_Nome(self):
		return self.__Nome
	
	def addIscritto(self, iscritto):
		self.listaIscritti.append(iscritto)
		
	def get_listaIscritti(self):
		return self.__listaIscritti
		
	def trovaIscritto(self, nome):
		flag=False
		for iscritto in self.listaIscritti:
			if iscritto.get_Nome() == nome:
				print(f"{nome} è iscritto!")
				flag=True
		if flag==False:
			print(f"{nome} non è iscritto")
		
	def trovaDiscipline(self, nome):
		pass
		
# main
def main():
	circolo=Circolo()
	
	nuoto=Nuoto("Nuoto", 200)
	aerobica=Aerobica("Aerobica", 100)
	bodybuilding=Bodybuilding("Bodybuilding", 130)
	
	iscritto1=Iscritto("Mario", "Rossi")
	iscritto2=Iscritto("Lorenzo", "Bianchi")
	iscritto3=Iscritto("Marco", "Rossi")
	
	iscritto1.addCorsi(nuoto)
	iscritto2.addCorsi(aerobica)
	iscritto3.addCorsi(bodybuilding)
	
	circolo.addIscritto(iscritto1)
	circolo.addIscritto(iscritto2)
	circolo.addIscritto(iscritto3)
	
	cerca_nome=input("Inserisci il nome da cercare: ")
	circolo.trovaIscritto(cerca_nome)
main()
