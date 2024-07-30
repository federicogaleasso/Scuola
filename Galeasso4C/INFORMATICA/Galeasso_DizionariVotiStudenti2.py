#GALEASSO FEDERICO 4C 13/11/2022 COMPITO - VOTI STUDENTI 2.0 CON L'USO DEI DIZIONARI

#Esercizio Voti Studenti 2.0
#Partendo dall'esercizio dei voti alunni, memorizzare nel codice PY, per alcuni studenti di esempio, una sequenza di voti a testa (invece di uno solo) con associata la data di quando è stata ricevuta ogni valutazione.
#Dato il nome di uno studente stampare l'elenco dei suoi voti in ordine crescente. Se lo studente non esiste, segnalarlo.
#Di ogni voto (stampati in ordine DEcrescente) elencare tutti i nomi degli studenti che l'hanno ricevuto indipendentemente dalla data.
#Chiesta in input una data, verificata la sua esistenza nel dizionario, stampare tutti i voti e i relativi nomi degli studenti che hanno ricevuto una votazione in tale giorno.

import os
def clearScreen():
	os.system("clear")
clearScreen()

ordinamento=0
trovato=0

diz={
	'Gino':{7:'12-04-2021',3.5:'09-06-2021'},
	'Lino':{7.5:'14-02-2021',4.5:'09-06-2021'},
	'Pia':{7:'09-06-2021',8:'09-09-2020'}
}

nome=input("Inserisci il nome da cercare nel dizionario: ")
while len(nome)==0:
	nome=input("ERRORE! Inserisci il nome da cercare nel dizionario: ")
for nomeFor in diz:
	if nomeFor==nome:
		trovato=1
		ordinamento=sorted(diz[nomeFor])	
if trovato==1:
	print("Nome trovato!")
	print("Voti:")
	for votiFor in ordinamento:
		print("-",votiFor)
if trovato==0:
	print("Nome non trovato!")
