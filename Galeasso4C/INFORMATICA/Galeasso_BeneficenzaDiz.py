#GALEASSO FEDERICO 4C 27/11/2022 COMPITO IN PREPARAZIONE ALLA VERIFICA SUI DIZIONARI - PESCA DI BENEFICENZA CON DIZIONARI

#La Proloco di Pecetto organizza la pesca di beneficenza e chiede aiuto ai concittadini per donare degli oggetti in buono stato da mettere come premi.
#La Proloco riesce a raccogliere X oggetti donati (X è dato in input dall’utente) che vengono memorizzati in un dizionario i cui elementi hanno come chiave un numero progressivo (da 1 a X) e come valore associato la descrizione dell’oggetto.
#Il programma deve permettere di registrare gli X oggetti donati, quindi presentare un menu che consenta di:
#1. Stampare gli oggetti già presenti nel dizionario in ordine progressivo di chiave numerica
#2. Eliminare un premio dal dizionario chiedendo all’utente il numero della chiave abbinata (se la chiave non esiste, segnalare l’errore)
#3. Ricercare un premio inserendo in input la sua descrizione.

import os
def clearScreen():
	os.system("clear")
clearScreen()

dizOggetti={}

print(f"{'*'*5} BENVENUTO NELLA PESCA DI BENEFICENZA {'*'*5}\n")

def chiediX():
	j=1
	X=int(input("Inserisci il numero di oggetti donati: "))
	for numero in range(X):
		oggetto=input(f"Inserisci il {j}° oggetto: ")
		j+=1
		dizOggetti[numero+1]=oggetto

def stampaDiz():
	for oggetto in dizOggetti:
		print(f"Numero: {oggetto} | Oggetto: {dizOggetti[oggetto]}")

def eliminaPremio():
	elimina=int(input("Elimina un premio inserendo il suo numero: "))
	if elimina in dizOggetti:
		print("Premio trovato, eliminazione in corso...")
		dizOggetti.pop(elimina)
	else:
		print("Premio non trovato")
	
def ricercaPremio():
	flag=True
	ricerca=input("Ricerca un premio inserendo la sua descrizione: ")
	for i in dizOggetti.items():
		if ricerca == i[1]:
			print("Premio trovato")
			print(f"Numero: {i[0]} | Oggetto: {i[1]}")
			flag=False
		else:
			if flag!=False:
				flag=True
	if flag==True:
		print("Premio non trovato")
		

def menu():
	chiediX()
	flag=True
	while flag==True:
		scelta=int(input("""
Scegli una di queste voci (0 per uscire):
1. Stampa il dizionario
2. Elimina un premio
3. Ricerca un premio inserendo la sua descrizione

--> """))
		
		if scelta==0:
			print("Arrivederci!")
			flag=False
		if scelta==1:
			stampaDiz()
		if scelta==2:
			eliminaPremio()
		if scelta==3:
			ricercaPremio()
		if scelta<0 or scelta>3:
			print("Scelta non valida!")

menu()	
