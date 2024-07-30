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
flag=False

while flag==False:
	N=input("Inserisci il numero degli studenti (>=1) --> ")
	try:
		numimmesso=int(N)
		flag=True
	except:
		print("ERRORE! Non hai messo un numero")
for i in range(numimmesso):
	print("\n---STUDENTE {}---".format(i+1))
	nome=input("Inserisci il nome del {}° studente --> ".format(i+1))
	
	flag=False
	while flag==False:
		altezza=input("Inserisci l'altezza del {}° studente --> ".format(i+1))
		try:
			altezzaimmessa=int(altezza)
			flag=True
		except:
			print("ERRORE! Non hai messo un numero")
	
	lista.append(nome)
	lista.append(altezzaimmessa)
	
	if altezzaimmessa>150:
		sottolistaMAX.append(altezzaimmessa)
		
	if altezzaimmessa<=150:
		sottolistaMIN.append(altezzaimmessa)
		
	if altezzaimmessa>MAX:
		MAX = altezzaimmessa
		altezzaMAX=altezzaimmessa
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
