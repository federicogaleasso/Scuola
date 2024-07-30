#GALEASSO FEDERICO 4C 19/1/2023 ESERCIZIO IN CLASSE - MULTE OOP

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Veicolo():
	def __init__(self, targa='', potenza=0, tipo=''):
		self.set_targa(targa)
		self.set_potenza(potenza)
		self.set_tipo(tipo)
		  
	def set_targa(self, targa):
		self.__targa = targa
		
	def get_targa(self):
		return self.__targa
		
	def set_potenza(self, potenza):
		self.__potenza = potenza
		
	def get_potenza(self):
		return self.__potenza
		
	def set_tipo(self, tipo):
		self.__tipo = tipo
		
	def get_tipo(self):
		return self.__tipo
		
	def __str__(self):
		return f'Targa: {self.__targa} | Potenza: {self.__potenza} | Tipo: {self.__tipo}'

class Auto(Veicolo):
	def __init__(self, targa='', potenza=0, marca=''):
		super().__init__(targa, potenza, 'Auto')
		self.set_marca(marca)
		
	def set_marca(self, marca):
		self.__marca = marca
		
	def get_marca(self):
		return self.__marca
		
	def __str__(self):
		return f'{super().__str__()} | Marca: {self.__marca}'
		
	
class Moto(Veicolo):
	def __init__(self, targa='', potenza=0, marca=''):
		super().__init__(targa, potenza, 'Moto')
		self.set_marca(marca)
		
	def set_marca(self, marca):
		self.__marca = marca
		
	def get_marca(self):
		return self.__marca
		
	def __str__(self):
		return f'{super().__str__()} | Marca: {self.__marca}'
		
class Multa():
	def __init__(self, numverbale=0, luogo='', veicolo=''):
		self.set_numverbale(numverbale)
		self.set_luogo(luogo)
		self.set_veicolo(veicolo)
		  
	def set_numverbale(self, numverbale):
		self.__numverbale = numverbale
		
	def get_numverbale(self):
		return self.__numverbale
		
	def set_luogo(self, luogo):
		self.__luogo = luogo
		
	def get_luogo(self):
		return self.__luogo
		
	def set_veicolo(self, veicolo):
		self.__veicolo = veicolo
		
	def get_veicolo(self):
		return self.__veicolo
		
	def __str__(self):
		return f'Numero verbale: {self.__numverbale} | Luogo: {self.__luogo} | Veicolo: {self.__veicolo}'
		
class Vigile():
	def __init__(self, nome='', matricola=''):
		self.set_nome(nome)
		self.set_matricola(matricola)
		self.lista_veicoli = []
		  
	def set_nome(self, nome):
		self.__nome = nome
		
	def get_nome(self):
		return self.__nome
		
	def set_matricola(self, matricola):
		self.__matricola = matricola
		
	def get_matricola(self):
		return self.__matricola
	
	def aggiungiVeicolo(self, targa, potenza, tipo, marca):
		if tipo == "Auto":
			veicolo = Auto(targa, potenza, marca)
		if tipo == "Moto":
			veicolo = Moto(targa, potenza, marca)
		self.lista_veicoli.append(veicolo)
		return veicolo
		
	def stampaVeicoli(self):
		for veicolo in self.lista_veicoli:
			print(veicolo)
	
	#def __str__(self):
		#return f'Nome: {self.__nome} | Matricola: {self.__matricola}'
		
def main():
	vigile=Vigile()
	auto1=vigile.aggiungiVeicolo("GF635RR", 1000, "Auto", "Ferrari")
	moto1=vigile.aggiungiVeicolo("AA981MG", 2000, "Moto", "BMW")
	vigile.stampaVeicoli()
main()
