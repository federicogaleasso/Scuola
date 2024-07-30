#GALEASSO FEDERICO 4C 29/1/2023 ESERCIZIO IN PREPARAZIONE ALLA VERIFICA - CORRIDA OOP

import os
def clearScreen():
	os.system("clear")
clearScreen()

#classe Esibizione()
class Esibizione():
	def __init__(self, titolo='', durata=0):
		self.set_titolo(titolo)
		self.set_durata(durata)
		
	def set_titolo(self, titolo):
		self.__titolo = titolo
		
	def get_titolo(self):
		return self.__titolo
		
	def set_durata(self, durata):
		self.__durata = durata
		
	def get_durata(self):
		return self.__durata
		
	def __repr__(self):
		return f'Titolo: {self.__titolo} | Durata: {self.__durata}'

# classe Canto(Esibizione)
class Canto(Esibizione):
	def __init__(self, titolo='', durata=0, genMusic=''):
		super().__init__(titolo, durata)
		self.set_genMusic(genMusic)
		
	def set_genMusic(self, genMusic):
		self.__genMusic = genMusic
		
	def get_genMusic(self):
		return self.__genMusic
	
	def __repr__(self):
		return f'{super().__repr__()} - Genere Musicale: {self.__genMusic}'
		
# classe Ginnastica(Esibizione)
class Ginnastica(Esibizione):
	def __init__(self, titolo='', durata=0, attrezzo=''):
		super().__init__(titolo, durata)
		self.set_attrezzo(attrezzo)
		
	def set_attrezzo(self, attrezzo):
		self.__attrezzo = attrezzo
		
	def get_attrezzo(self):
		return self.__attrezzo
	
	def __repr__(self):
		return f'{super().__repr__()} - Attrezzo: {self.__attrezzo}'

# classe Poesia(Esibizione)
class Poesia(Esibizione):
	def __init__(self, titolo='', durata=0):
		super().__init__(titolo, durata)
	
	def __repr__(self):
		return f'{super().__repr__()}'
		
#classe Partecipante()
class Partecipante():
	def __init__(self, nome='', cognome='', sesso='', eta=0, tipologia=''):
		self.set_nome(nome)
		self.set_cognome(cognome)
		self.set_sesso(sesso)
		self.set_eta(eta)
		self.set_tipologia(tipologia)
		
	def set_nome(self, nome):
		self.__nome = nome
		
	def get_nome(self):
		return self.__nome
		
	def set_cognome(self, cognome):
		self.__cognome = cognome
		
	def get_cognome(self):
		return self.__cognome
		
	def set_sesso(self, sesso):
		self.__sesso = sesso
		
	def get_sesso(self):
		return self.__sesso
		
	def set_eta(self, eta):
		self.__eta = eta
		
	def get_eta(self):
		return self.__eta
		
	def set_tipologia(self, tipologia):
		self.__tipologia = tipologia
		
	def get_tipologia(self):
		return self.__tipologia
	
	def __repr__(self):
		return f'Nome: {self.__nome} | Cognome: {self.__cognome} | Sesso: {self.__sesso} | Eta: {self.__eta} | Tipologia: {self.__tipologia}'
		
#classe Manifestazione()
class Manifestazione():
	def __init__(self, nome='', listapartecipanti=[], elencoCantanti={}, elencoPoeti={}, elencoGinnasti={}):
		self.set_nome(nome)
		self.__listapartecipanti=listapartecipanti
		self.__elencoCantanti=elencoCantanti
		self.__elencoPoeti=elencoPoeti
		self.__elencoGinnasti=elencoGinnasti
		
	def set_nome(self, nome):
		self.__nome = nome
		
	def get_nome(self):
		return self.__nome
	
	def aggiungiPartecipante(self, partecipante):
		self.__listapartecipanti.append(partecipante)
		
	def get_listapartecipanti(self):
		return self.__listapartecipanti
		
	def aggiungiCantante(self, partecipante, canto):
		self.__elencoCantanti[partecipante]=canto
		
	def get_elencoCantanti(self):
		return self.__elencoCantanti
	
	def aggiungiGinnasta(self, partecipante, ginnastica):
		self.__elencoGinnasti[partecipante]=ginnastica
		
	def get_elencoGinnasti(self):
		return self.__elencoGinnasti
	
	def aggiungiPoeta(self, partecipante, poesia):
		self.__elencoPoeti[partecipante]=poesia
		
	def get_elencoPoeti(self):
		return self.__elencoPoeti
	
	def trova(self, nome, cognome):
		for part in self.get_listapartecipanti():
			if part.get_nome() == nome and part.get_cognome() == cognome:
				if part.get_tipologia() != "Canto" or part.get_tipologia() != "Ginnastica" or part.get_tipologia() != "Poesia":
					print(f"{nome} {cognome} è un partecipante semplice")
					return part
				if part.get_tipologia() == "Canto" or part.get_tipologia() == "Ginnastica" or part.get_tipologia() == "Poesia":
					print(f"La performance di {nome} {cognome} si intitola ... e dura ...")
					return part
		print(f"{nome} {cognome} non è un partecipante")
	
	def __repr__(self):
		return f'{self.__nome}'
	
# main()	
def main():
	manifestazione=Manifestazione("LA CORRIDA")
	print(manifestazione,"\n")
	
	canto=Canto("Canto", 120, "Rap")
	ginnastica=Ginnastica("Ginnastica", 20, "Sbarra")
	poesia=Poesia("Poesia", 40)
	
	print(canto)
	print(ginnastica)
	print(poesia)
	
	print("\n")
	
	p1=Partecipante("Mario", "Rossi", "M", 20, "Null")
	p2=Partecipante("Giulia", "Rosso", "F", 12, "Canto")
	p3=Partecipante("Francesco", "Bianco", "M", 40, "Canto")
	p4=Partecipante("Veronica", "Martini", "F", 23, "Ginnastica")
	p5=Partecipante("Federico", "Angaramo", "M", 25, "Ginnastica")
	p6=Partecipante("Flavio", "Olivero", "M", 18, "Poesia")
	
	manifestazione.aggiungiPartecipante(p1)
	manifestazione.aggiungiPartecipante(p2)
	manifestazione.aggiungiPartecipante(p3)
	manifestazione.aggiungiPartecipante(p4)
	manifestazione.aggiungiPartecipante(p5)
	manifestazione.aggiungiPartecipante(p6)
	
	for part in manifestazione.get_listapartecipanti():
		print(part)
	
	print("\nElenco Cantanti")
	manifestazione.aggiungiCantante(p2, canto)
	manifestazione.aggiungiCantante(p3, canto)
	for part in manifestazione.get_elencoCantanti().items():
		print(part[0]," # ",part[1])
		
	print("\nElenco Ginnasti")
	manifestazione.aggiungiGinnasta(p4, ginnastica)
	manifestazione.aggiungiGinnasta(p5, ginnastica)
	for part in manifestazione.get_elencoGinnasti().items():
		print(part[0]," # ",part[1])
		
	print("\nElenco Poeti")
	manifestazione.aggiungiPoeta(p6, poesia)
	for part in manifestazione.get_elencoPoeti().items():
		print(part[0]," # ",part[1])
	
	nome=input("\nInserisci il nome da cercare: ")
	cognome=input("Inserisci il conome da cercare: ")
	manifestazione.trova(nome, cognome)
main()
