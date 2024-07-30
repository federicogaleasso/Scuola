#GALEASSO FEDERICO 4C 20/2/2023 COMPITO - OSPEDALE OOP

import os
import random

def clearScreen():
	os.system("clear")
clearScreen()

#classe Ospedale()
class Ospedale():
	def __init__(self, Nome='', Reparti=[]):
		self.set_Nome(Nome)
		self.__Reparti=Reparti
		
	def set_Nome(self, Nome):
		self.__Nome = Nome
		
	def get_Nome(self):
		return self.__Nome
		
	def aggiungiReparti(self, reparto):
		self.__Reparti.append(reparto)
	
	def visualizzaReparti(self):
		for reparto in self.__Reparti:
			print(reparto)			
	
	def __str__(self):
		return f'Ospedale "{self.get_Nome()}"\n'
		
#classe Reparto()
class Reparto():
	def __init__(self, denominazione='', nLetti=0, Personale=[], Pazienti=[]):
		self.set_denominazione(denominazione)
		self.set_nLetti(nLetti)
		self.__Personale=Personale
		self.__Pazienti=Pazienti
		
	def set_denominazione(self, denominazione):
		self.__denominazione = denominazione
		
	def get_denominazione(self):
		return self.__denominazione
	
	def set_nLetti(self, nLetti):
		self.__nLetti = nLetti
		
	def get_nLetti(self):
		return self.__nLetti
		
	def aggiungiPersonale(self, personale):
		self.__Personale.append(personale)
		
	def visualizzaPersonale(self):
		for personale in self.__Personale:
			print(personale)
		
	def aggiungiPazienti(self, paziente):
		self.__Pazienti.append(paziente)
		
	def visualizzaPazienti(self):
		for paziente in self.__Pazienti:
			print(paziente)
			
	def dimettiPaziente(self, nome, cognome):
		print("Pazienti dimessi:")
		for paziente in self.__Pazienti:
			if paziente.get_Nome() == nome and paziente.get_Cognome() ==cognome:
				self.__Pazienti.remove(paziente)
				print(f"Il paziente {paziente.get_Nome()} {paziente.get_Cognome()} è stato dimesso\n")
				return paziente
	
	def __str__(self):
		return f'Denominazione: {self.get_denominazione()}\nNumeri di letti: {self.get_nLetti()}\n'
		
#classe Persona()
class Persona():
	def __init__(self, Nome='', Cognome='', CodiceFiscale='', dataNascita=''):
		self.set_Nome(Nome)
		self.set_Cognome(Cognome)
		self.set_CodiceFiscale(CodiceFiscale)
		self.set_dataNascita(dataNascita)
		
	def set_Nome(self, Nome):
		self.__Nome = Nome
		
	def get_Nome(self):
		return self.__Nome
		
	def set_Cognome(self, Cognome):
		self.__Cognome = Cognome
		
	def get_Cognome(self):
		return self.__Cognome
		
	def set_CodiceFiscale(self, CodiceFiscale):
		self.__CodiceFiscale = CodiceFiscale
		
	def get_CodiceFiscale(self):
		return self.__CodiceFiscale
	
	def set_dataNascita(self, dataNascita):
		self.__dataNascita = dataNascita
		
	def get_dataNascita(self):
		return self.__dataNascita
	
	def __str__(self):
		return f'Nome: {self.get_Nome()}\nCognome: {self.get_Cognome()}\nCodice Fiscale: {self.get_CodiceFiscale()}\nData di nascita: {self.get_dataNascita()}\n'
		
#classe Paziente(Persona)
class Paziente(Persona):
	def __init__(self, Nome='', Cognome='', CodiceFiscale='', dataNascita='', motivoRicovero='', dataRicovero=''):
		super().__init__(Nome, Cognome, CodiceFiscale, dataNascita)
		self.set_motivoRicovero(motivoRicovero)
		self.set_dataRicovero(dataRicovero)
		
	def set_motivoRicovero(self, motivoRicovero):
		self.__motivoRicovero = motivoRicovero
		
	def get_motivoRicovero(self):
		return self.__motivoRicovero
	
	def set_dataRicovero(self, dataRicovero):
		self.__dataRicovero = dataRicovero
		
	def get_dataRicovero(self):
		return self.__dataRicovero
	
	def __str__(self):
		return f'{super().__str__()}Motivo del ricovero: {self.get_motivoRicovero()}\nData del ricovero: {self.get_dataRicovero()}\n'
		
#classe Personale(Persona)
class Personale(Persona):
	def __init__(self, Nome='', Cognome='', CodiceFiscale='', dataNascita='', Matricola='', livelloQualifica=0, reparto=''):
		super().__init__(Nome, Cognome, CodiceFiscale, dataNascita)
		self.set_Matricola(Matricola)
		self.set_livelloQualifica(livelloQualifica)
		self.set_reparto(reparto)
		
	def set_Matricola(self, Matricola):
		self.__Matricola = Matricola
		
	def get_Matricola(self):
		return self.__Matricola
	
	def set_livelloQualifica(self, livelloQualifica):
		self.__livelloQualifica = livelloQualifica
		
	def get_livelloQualifica(self):
		return self.__livelloQualifica
		
	def set_reparto(self, reparto):
		self.__reparto = reparto
		
	def get_reparto(self):
		return self.__reparto
	
	def __str__(self):
		return f'{super().__str__()}Matricola: {self.get_Matricola()}\nLivello di qualifica: {self.get_livelloQualifica()}\nREPARTO:\n{self.get_reparto()}'

# main()
def main():
	ospedale=Ospedale("Regina Margherita")
	print(ospedale)
	
	nLetti=random.randint(4,25)
	Medicina=Reparto("Medicina", nLetti)
	ospedale.aggiungiReparti(Medicina)
	
	nLetti=random.randint(4,25)
	Chirurgia=Reparto("Chirurgia", nLetti)
	ospedale.aggiungiReparti(Chirurgia)
	
	nLetti=random.randint(4,25)
	Ortopedia=Reparto("Ortopedia", nLetti)
	ospedale.aggiungiReparti(Ortopedia)
	
	Reparti=Reparto("", nLetti)
	
	print("REPARTI:\n")
	ospedale.visualizzaReparti()
	
	paziente1=Paziente("Mario", "Rossi", "RSSMRA93T09D205I", "09/12/1993", "Polmonite", "20/2/2023")
	paziente2=Paziente("Luca", "Rossa", "LCURSS75P05D205Y", "05/09/1975", "Tumore al cuore", "18/2/2023")
	paziente3=Paziente("Giulia", "Bianchi", "GLIBCH01D43D205V", "03/04/2001", "Frattura alla caviglia", "30/1/2023")
	
	Medicina.aggiungiPazienti(paziente1)
	Chirurgia.aggiungiPazienti(paziente2)
	Ortopedia.aggiungiPazienti(paziente3)
	
	print("PAZIENTI:\n")
	Reparti.visualizzaPazienti()
	
	personale1=Personale("Mattia", "Gialli", "MTTGLL70M05D205L", "05/08/1970", "AB123456", 1, Medicina)
	personale2=Personale("Lorenzo", "Neri", "LRNNRE76T14D205E", "14/12/1976", "GH178295", 4, Chirurgia)
	personale3=Personale("Anna", "Verde", "NNAVRD94P48D205I", "08/09/1994", "KA019526", 3, Ortopedia)
	
	Medicina.aggiungiPersonale(personale1)
	Chirurgia.aggiungiPersonale(personale2)
	Ortopedia.aggiungiPersonale(personale3)
	
	print("PERSONALE:\n")
	Reparti.visualizzaPersonale()
	
	Reparti.dimettiPaziente("Mario", "Rossi")
	
	print("Ecco la lista dei pazienti aggiornata:\n")
	Reparti.visualizzaPazienti()
main()
