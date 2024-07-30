#GALEASSO FEDERICO 4C 30/10/2022 COMPITO - IL LINGUAGGIO DEI FURFANTI

#Il linguaggio dei furfanti
#In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
#Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".
#Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova frase da parte dell'utente.
#Usare stringhe, liste o tuple a piacere e in base alla necessità.

import os
def clearScreen():
	os.system("clear")
clearScreen()

def traduttore():
	flag=True
	input(f"{'*'*5} BENVENUTO {'*'*5}\nCon questo traduttore puoi tardurre frasi o parole nel linguaggio dei furfanti, detto anche rövarspråket.\nPremi invio per continuare...")
	clearScreen()
	while flag==True:
		lista=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
		testo=input("Inserisci il testo da tradurre --> ")
		while len(testo)==0:
			testo=input("ERRORE, testo vuoto!!! Inserisci il testo da tradurre --> ")
		testo_tradotto=""
		for carattere in testo:
			if carattere in lista:
				testo_tradotto=testo_tradotto+carattere+"o"+carattere
			else:
				testo_tradotto=testo_tradotto+carattere
		print(f"Ecco la frase tradotta --> {testo_tradotto}")
		continuare=input("\nVuoi tradurre un'altre frase? Inserisci 'no' per uscire --> ");
		if continuare=="no":
			flag=False
traduttore()
