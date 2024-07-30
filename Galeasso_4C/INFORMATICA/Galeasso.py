#GALEASSO FEDERICO 4C 10/10/2022 VERIFICA

import os
def clearScreen():
	os.system("clear")
clearScreen()

i=0
j=1
veicoli=[]
margini=[]

N=int(input("Inserisci il numero dei veicoli (compreso tra 2 e 8) --> "))
while N<2 or N>8:
	N=int(input("ERRORE! Inserisci il numero dei veicoli (compreso tra 2 e 8) --> "))
print("\n")
for i in range(N):
	print("---VEICOLO {}---".format(i+1))
	targa=input("Inserisci la targa del {}° veicolo (7 caratteri) --> ".format(i+1))
	while not len(targa)==7:	 #or isinstance(targa[2:4], int)==False
		targa=input("ERRORE! Inserisci la targa del {}° veicolo (7 caratteri) --> ".format(i+1))
	colore=input("Inserisci il colore del {}° veicolo --> ".format(i+1))
	prezzo=int(input("Inserisci il prezzo del {}° veicolo --> ".format(i+1)))
	veicoli.append((targa,colore,prezzo))
	print("\n")
for el in veicoli:
	print(f"---VEICOLO {j}---\n")
	print(f"{el}\n\n")
	j+=1

searchcolor=input("Inserisci il colore da cercare --> ")
#for i in range(N):
	#if veicoli.index(searchcolor):
		#print(veicoli[i])

for i in range(4):
	targa2=input("Inserisci la targa del veicolo da acquistare (7 caratteri) --> ")
	while not len(targa2)==7:	 #or isinstance(targa[2:4], int)==False
		targa2=input("ERRORE! Inserisci la targa del veicolo da acquistare (7 caratteri) --> ".format(i+1))
	prezzo2=int(input("Inserisci il prezzo del veicolo da acquistare --> "))
	#if veicoli.index(targa2):
		#print("La targa non è presente nella lista")
	if	prezzo2<prezzo:
		print("Prezzo non sufficente")
	
	if prezzo2>prezzo:
		margini.append()
