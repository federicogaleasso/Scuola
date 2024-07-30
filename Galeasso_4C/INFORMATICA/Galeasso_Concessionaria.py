#GALEASSO FEDERICO 4C 14/1/2023 COMPITO CONCESSIONARIA OOP

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Autoveicolo:
	def __init__(self, targa='', modello=''):
		self.set_targa(targa)
		self.set_modello(modello)
		  
	def set_targa(self, targa):
		self.__targa = targa
		
	def get_targa(self):
		return self.__targa
		
	def set_modello(self, modello):
		self.__modello = modello
		
	def get_modello(self):
		return self.__modello
		
	def __str__(self):
		return f'Targa: {self.__targa} | Modello: {self.__modello}'

class VeicoloPrivato(Autoveicolo):
	def __init__(self, targa='', modello='', numeroPorte=0, numeroPosti=0):
		super().__init__(targa, modello)
		self.set_numeroPorte(numeroPorte)
		self.set_numeroPosti(numeroPosti)
        
	def set_numeroPorte(self, numeroPorte):
		self.__numeroPorte = numeroPorte
		
	def get_numeroPorte(self):
		return self.__numeroPorte
		
	def set_numeroPosti(self, numeroPosti):
		self.__numeroPosti = numeroPosti
		
	def get_numeroPosti(self):
		return self.__numeroPosti
		
	def __str__(self):
		return f'{super().__str__()} | Numero Porte: {self.__numeroPorte} | Numero Posti: {self.__numeroPosti}'

class VeicoloCommerciale(Autoveicolo):
	def __init__(self, targa='', modello='', pesoCarico=0, pesoVuoto=0, articolato=True):
		super().__init__(targa, modello)
		self.set_pesoCarico(pesoCarico)
		self.set_pesoVuoto(pesoVuoto)
		self.set_articolato(articolato)
        
	def set_pesoCarico(self, pesoCarico):
		self.__pesoCarico = pesoCarico
		
	def get_pesoCarico(self):
		return self.__pesoCarico
		
	def set_pesoVuoto(self, pesoVuoto):
		self.__pesoVuoto = pesoVuoto
		
	def get_pesoVuoto(self):
		return self.__pesoVuoto
		
	def set_articolato(self, articolato):
		self.__articolato = articolato
		
	def get_articolato(self):
		return self.__articolato
		
	def __str__(self):
		return f'{super().__str__()} | Peso Carico: {self.__pesoCarico} | Peso Vuoto: {self.__pesoVuoto} | Articolato: {self.__articolato}'
		
class Concessionario:
	def __init__(self, nome='', veicoli=[]):
		self.set_nome(nome)
		self.set_veicoli(veicoli)
        
	def CompraVeicolo(self, veicolo):
		self.__veicoli.append(veicolo)
        
	def VendiVeicolo(self, targa):
		for veicolo in self.__veicoli:
			if veicolo.get_targa() == targa:
				print(f"Targa trovata! Il veicolo con targa {targa} verrà rimosso.")
				self.__veicoli.remove(veicolo)
				
	def get_veicoli(self):
		return self.__veicoli
	
	def set_veicoli(self, veicoli):
		self.__veicoli = veicoli
		
	def get_nome(self):
		return self.__nome
	
	def set_nome(self, nome):
		self.__nome = nome

def main():
	concessionario = Concessionario()

	concessionario.CompraVeicolo(VeicoloCommerciale("AE957CC", "VeicoloCommerciale1", 15364, 2918, False))
	concessionario.CompraVeicolo(VeicoloCommerciale("GE174EF", "VeicoloCommerciale2", 21935, 4152, True))
	concessionario.CompraVeicolo(VeicoloPrivato("BA916DD", "VeicoloPrivato1", 4, 5))
	
	j=1
	print("Ecco i veicoli stampati")
	for veicolo in concessionario.get_veicoli():
		print(f"\n{'*'*5} {'VEICOLO'} {j} {'*'*5}")
		print(veicolo)
		j+=1
		
	cerca_targa=input("\nInserisci la targa da ricercare: ")
	concessionario.VendiVeicolo(cerca_targa)
	
	j=1
	print("\nEcco i veicoli stampati dopo la ricerca della targa")
	for veicolo in concessionario.get_veicoli():
		print(f"\n{'*'*5} {'VEICOLO'} {j} {'*'*5}")
		print(veicolo)
		j+=1
main()
