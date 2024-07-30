#GALEASSO FEDERICO 4C 6/11/2022 COMPITO - PRODOTTI CON MODULI E FUNZIONI

#Da tastiera vengono introdotti per n prodotti il nome del prodotto, la quantità venduta e il prezzo unitario. Calcola il prezzo medio, la quantità media e il valore totale delle vendite (sommatoria dei prezzi per le quantità). Organizza le funzioni di calcolo in un modulo. La funzione per il calcolo della media viene usata due volte, per la media dei prezzi e per la media delle quantità.

import os
import Galeasso_ModuloProdotti as modulo

def clearScreen():
	os.system("clear")
clearScreen()

j=0
prezzoTot=0
quantitaTot=0

n=int(input("Inserisci il numero di prodotti: "))
while n<=0:
	n=int(input("ERRORE! Reinserisci il numero di prodotti: "))
for prodotto in range(n):
	j+=1
	print(f"\n{'*'*5} {'PRODOTTO'} {j} {'*'*5}")
	nome=input(f"Inserisci il NOME del {j}° prodotto: ")
	while len(nome)==0:
		nome=input(f"ERRORE! Reinserisci il NOME del {j}° prodotto: ")
	quantita=int(input(f"Inserisci la QUANTITÀ del {j}° prodotto: "))
	while quantita<=0:
		quantita=int(input(f"ERRORE! Reinserisci la QUANTITÀ del {j}° prodotto: "))
	prezzo=float(input(f"Inserisci il PREZZO del {j}° prodotto: "))
	while prezzo<=0:
		prezzo=float(input(f"ERRORE! Reinserisci il PREZZO del {j}° prodotto: "))
	quantitaTot+=quantita
	prezzoTot+=prezzo

modulo.mediaPrezziQuantita(quantitaTot,prezzoTot,n)
modulo.venditeTotali(quantitaTot,prezzoTot)
