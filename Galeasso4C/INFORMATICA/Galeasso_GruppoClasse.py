#GALEASSO FEDERICO 4C 5/1/2023 ESERCIZIO VACANZE NATALIZIE GRUPPO CLASSE

import os
def clearScreen():
	os.system("clear")
clearScreen()

#Classe Studente()
class Studente():
	def __init__(self, voti):
		self.__voti = []
		self.setVoti(voti)
		
	def setVoti(self, voti):
		self.__voti.append(voti)
		if (self.__voti[0]) == 0:
			del self.__voti[0]
		
	def getVoti(self):
		return self.__voti

#Classe Persona()	
class Persona():
	def __init__(self, nome=0, cognome=0):
		self.setNomep(nome)
		self.setCognome(cognome)
		
	def setNomep(self, nome):
		self.__nome = nome
		
	def getNomep(self):
		return self.__nome
		
	def setCognome(self, cognome):
		self.__cognome = cognome
		
	def getCognomep(self):
		return self.__cognome

#Classe GruppoClasse()
class GruppoClasse():
	def __init__(self, nome, elencostud):
		self.__elenco = []
		self.nome = nome
		self.setelencostud(elencostud)
		
	def setelencostud(self, elencostud):
		self.__elenco.append(elencostud)
		if len(self.__elenco[0]) == 0:
			del self.__elenco[0]
		
	def getelencostud(self):
		return self.__elenco
	
	#funzione aggiungistud()
	def aggiungistud(self, Persona):
		nome=input("Inserisci il nome del nuovo studente: ")
		cognome=input("Inserisci il cognome del nuovo studente: ")
		aggiungiStud=Persona(nome, cognome)
		self.setelencostud([nome, cognome])
		print("Studente aggiunto!")
	
	#funzione aggiungivoto()
	def aggiungivoto(self, Studente):
		i=0
		pos=0
		cognome_aggiungiVoto=input("Inserisci il cognome dello studente: ")
		for z in self.getelencostud():
			if z[1]==cognome_aggiungiVoto:
				pos=i
				voto_aggiungiVoto=int(input("Inserisci il nuovo voto: "))
				voto=Studente
				votoStud=voto.getVoti()
				votoStud[pos].append(voto_aggiungiVoto)
				print("Voto aggiunto!")
				break
			i+=1
	
	#funzione rimuovis() 
	def rimuovis(self, Studente):
		i=0
		cognome_rimuovis=input("Inserisci il cognome da rimuovere: ")
		votoStud=Studente.getVoti()
		Stud=self.getelencostud()
		for Studente in Stud:
			if Studente[1]==cognome_rimuovis:
				del votoStud[i]
				del Stud[i]
				print("Studente rimosso!")
				break
			i+=1
	
	#funzione cercas()
	def cercas(self, Stud):
		pos=0
		nome_cercas=input("Inserisci il nome da cercare: ")
		cognome_cercas=input("Inserisci il cognome da cercare: ")
		elenco=self.getelencostud()
		voti=Stud.getVoti()
		for Studente in elenco:
			if Studente[0]==nome_cercas and Studente[1]==cognome_cercas:
				for i in range(len(voti[pos])):
					print(voti[pos][i])
			pos+=1

#funzione inserisciStudente()
def inserisciStudente(studente, gruppoclasse):
	lista_voti = []
	nome=input("Inserisci il nome dello studente: ")
	cognome=input("Inserisci il cognome dello studente: ")
	persona=Persona(nome, cognome)
	for x in range(2):
		voto = int(input("Inserisci il voto: "))
		lista_voti.append(voto)
	studente.setVoti(lista_voti)
	gruppoclasse.setelencostud([nome, cognome])

#main	
def main():
	j=1
	gruppoclasse=GruppoClasse("", [])
	studente=Studente(0)
	for i in range(2):
		print(f"{'*'*5} {'STUDENTE'} {j} {'*'*5}")
		inserisciStudente(studente, gruppoclasse)
		j+=1
	gruppoclasse.aggiungistud(Persona)
	gruppoclasse.aggiungivoto(studente)
	gruppoclasse.rimuovis(studente)
	gruppoclasse.cercas(studente)
main()	
