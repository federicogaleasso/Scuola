#GALEASSO FEDERICO 4C 30/9/2022 COMPITO TEMPERATURE CITTÀ

#Dato un elenco di città, con l’indicazione per ciascuna di esse del nome e delle temperature massima e minima registrate in un giorno, si devono #contare quante città hanno superato nel giorno un valore preﬁssato per l’escursione termica, ottenuta per differenza tra temperatura massima e #minima.
#Organizza un programma che, dopo aver richiesto il valore da controllare dell’escursione termica, per ogni città dell’elenco ripeta la richiesta #dei dati (nome, temperatura massima e minima), calcoli l’escursione termica e controlli se l’escursione è maggiore del valore preﬁssato:
#in questo caso, incrementa il contatore delle città selezionate. Alla ﬁne della ripetizione comunica il numero delle città registrato nel #contatore.

import os
def clearScreen():
	os.system("clear")
clearScreen()

N=int(input("Inserisci il numero di città (almeno 1!): "))
while N<1:
	clearScreen()
	N=int(input("ERRORE! Inserisci il numero di città (almeno 1!): "))
esctermica=int(input("Inserisci il valore dell'escursione termica: "))
lista=[]
contatore=0
for i in range(N):
	print("\n-CITTA' {}-".format(i+1))
	nome=input("Inserisci il nome della {}° città: ".format(i+1))
	tmax=int(input("Inserisci la temperatura massima della {}° città: ".format(i+1)))
	tmin=int(input("Inserisci la temperatura minima della {}° città: ".format(i+1)))
	esctermicacitta=tmax-tmin
	print("L'escursione termica della {}° città è:".format(i+1),esctermicacitta)
	if esctermicacitta>esctermica:
		contatore=contatore+1
print("\nIl numero di città che superano l'escursione termica "+"("+str(esctermica)+")"+" sono/è:",contatore)
