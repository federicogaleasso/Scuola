#GALEASSO FEDERICO 4C 6/10/2022 COMPITO ALTEZZE STUDENTI 

#Creare un programma in Python che svolga queste operazioni in sequenza:
#1. Riempi lista (chiedendo in input il numero di elementi di cui dovrà  essere composta), riempirla con i nomi degli studenti e la loro relativa altezza
#2. Partendo dalla lista precedente, crea la sottolista degli studenti che hanno altezza superiore a 150cm e una sottolista di studenti con altezza minore o uguale a 150cm
#3. Visualizza il nome dello studente con altezza maggiore
#4. Conta le istanze di entrambe le sottoliste (stabilire e visualizzare quale lista ha più elementi)

import os
def clearScreen():
	os.system("clear")
clearScreen()

lista=[]
sottolistaMAX=[]
sottolistaMIN=[]
MAX=0
altezzaMAX=0
nomeMAX=""

N=int(input("Inserisci il numero degli studenti (>=1) --> "))
while N<1:
	clearScreen()
	N=int(input("ERRORE! Inserisci il numero degli studenti (>=1) --> "))
for i in range(N):
	print("\n---STUDENTE {}---".format(i+1))
	nome=input("Inserisci il nome del {}° studente --> ".format(i+1))
	altezza=int(input("Inserisci l'altezza del {}° studente --> ".format(i+1)))
	lista.append(nome)
	lista.append(altezza)
	
	if altezza>150:
		sottolistaMAX.append(altezza)
		
	if altezza<=150:
		sottolistaMIN.append(altezza)
		
	if altezza>MAX:
		MAX = altezza
		altezzaMAX=altezza
		nomeMAX=nome
		
lista.append(sottolistaMAX)
lista.append(sottolistaMIN)
print("\nIl nome dello studente con altezza maggiore "+"("+str(altezzaMAX)+")"+" è:",nomeMAX)

if len(sottolistaMAX)>len(sottolistaMIN):
	print("\nLa sottolista degli studenti con altezza maggiore di 150 è quella con più elementi: "+str(len(sottolistaMAX))+"\nEcco la lista stampata:\n"+str(sottolistaMAX))
if len(sottolistaMIN)>len(sottolistaMAX):
	print("\nLa sottolista degli studenti con altezza minore o uguale a 150 è quella con più elementi: "+str(len(sottolistaMIN))+"\nEcco la lista stampata:\n"+str(sottolistaMIN))
if len(sottolistaMIN)==len(sottolistaMAX):
	print("\nLe 2 sottoliste hanno lo stesso numero di elementi "+"("+str(len(sottolistaMAX))+")")
