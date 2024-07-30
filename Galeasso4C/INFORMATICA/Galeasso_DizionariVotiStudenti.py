#GALEASSO FEDERICO 4C 11/11/2022 COMPITO - VOTI STUDENTI CON L'USO DEI DIZIONARI

#Esercizio Voti Studenti
#I voti assegnati a 30 studenti di una classe in una prova di italiano sono chiesti in input e
#memorizzati in un dizionario che ha per chiave il nome, mentre il valore associato è il voto.
#Elenca i risultati in ordine crescente di voto stampando per ciascuna valutazione la lista dei nomi degli alunni che l'hanno ricevuta.

import os
def clearScreen():
	os.system("clear")
clearScreen()

diz=dict()
i=0
j=1

for i in range(2):
	print(f"{'*'*5} {'STUDENTE'} {j} {'*'*5}")
	nome=input(f"Inserisci il nome del {j} studente: ")
	while len(nome)==0:
		nome=input(f"ERRORE! Inserisci il nome del {j} studente: ")
	voto=int(input(f"Inserisci il voto del {j} studente: "))
	while voto<2 or voto>10:
		voto=int(input(f"ERRROE! Inserisci il voto del {j} studente: "))
	j+=1
	diz[nome]=voto
	
print("\nEcco gli alunni e i relativi voti stampati")
print(diz)

print("\nEcco i voti ordinati in ordine crescente")
ordinamento = sorted(diz.values())
for voto in ordinamento:
	print("\nVoto:", voto)
	for nome in diz:
		if voto == diz[nome]:
			print("Alunno:",nome)
