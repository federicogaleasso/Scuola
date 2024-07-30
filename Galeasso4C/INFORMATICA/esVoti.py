#GALEASSO FEDERICO 4C 29/9/2022 COMPITO VOTI

#Esercizio Python Grafico Voti:
#chiedere all'utente quanti studenti hanno fatto la verifica di informatica;
#chiedere ciclicamente i nomi di questi studenti e il relativo voto ottenuto alla verifica;
#memorizzare nomi e voti in UNA sola lista;
#stampare l'elenco dei nomi degli studenti con a fianco un numero di '*' uguale al voto preso (voti tutti interi ovviamente) come una sorta di #grafico a barre orizzontali dei voti

import os
def clearScreen():
	os.system("clear")
clearScreen()

N=int(input("Quanti studenti hanno fatto la verifica di informatica (almeno 1 studente!)? "))
while N<1:
	clearScreen()
	N=int(input("ERRORE! Quanti studenti hanno fatto la verifica di informatica (almeno 1 studente!)? "))
lista=[]
for i in range(N):
	print("\n-STUDENTE {}-".format(i+1))
	nome=input("Inserisci il nome del {}° studente: ".format(i+1))
	voto=int(input("Inserisci il voto del {}° studente: ".format(i+1)))
	voto=("*"*voto)
	lista.append(nome)
	lista.append(voto)
for i in range(1):
	print("\nEcco la lista stampata!\n")
	print(lista[(i):])
