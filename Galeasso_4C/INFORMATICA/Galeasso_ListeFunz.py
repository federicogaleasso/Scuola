#GALEASSO FEDERICO 4C 22/10/2022 COMPITO - LISTE FUNZIONI E NON SOLO

#Creare un programma in Python che svolga queste operazioni in sequenza (ogni operazione è una funzione):
#1. Riempi lista (chiedendo in input il numero di elementi di cui dovrà essere composta e riempirla con valori random tra 0 e 100)
#2. Crea sottolista numeri pari e sottolista numeri dispari
#3. Esegui la somma di entrambe le sottoliste (stabilire e visualizzare in output quale lista ha la somma maggiore)
#4. Conta le istanze di entrambe le sottoliste (stabilire e visualizzare quale lista ha più elementi)
#5. Conta le istanze ripetute per ogni lista e visualizzare a video l’elemento ed il numero di istanze come sequenza di asterischi
#(es. 27: *** se il numero 27 è presente 3 volte nella lista).

import random
import os

def clearScreen():
	os.system("clear")
clearScreen()

lista=[]
sottolistaPari=[]
sottolistaDispari=[]
i=0
max=100
min=0

print(f"{'*'*5} BENVENUTO {'*'*5}\n")

#Funzione per la richiesta del numero
def chiediNumero():
	j=1
	N=int(input("Quanti numeri vuoi inserire (tra 1 e 10!)? --> "))
	while N<1 or N>10:
		N=int(input("ERRORE! Quanti numeri vuoi inserire (tra 1 e 10!)? --> "))
	print("\nEcco i numeri stampati...\n")
	for i in range(N):
		nrandom=random.randint(min,max)
		print(f"{' ':5}{'Numero'} {j}: {nrandom}")
		j+=1
		lista.append(nrandom)
	return N

#Funzione per controllare se il numero è pari o dispari
def pariDispari():
	for num in lista:
		if num%2==0:
			sottolistaPari.append(num)
		else:
			sottolistaDispari.append(num)
	print(f"\nEcco la sottolista dei numeri pari --> {sottolistaPari}")
	print(f"Ecco la sottolista dei numeri dispari --> {sottolistaDispari}\n")

#Funzione per la somma delle istanze delle due sottoliste
def sommaSottoliste():
	sommaPari=0
	sommaDispari=0
	for num in sottolistaPari:
		sommaPari=sommaPari+num
	for num in sottolistaDispari:
		sommaDispari=sommaDispari+num
	print("La somma dei numeri pari è:",sommaPari)
	print("La somma dei numeri dispari è:", sommaDispari,"\n")
	if sommaPari>sommaDispari:
		print("La somma della sottolista dei numeri pari","(",sommaPari,")","è maggiore di quella dei numeri dispari","(",sommaDispari,")\n")
	else:
		print("La somma della sottolista dei numeri dispari","(",sommaDispari,")","è maggiore di quella dei numeri pari","(",sommaPari,")\n")

#Funzione per controllare quale lista ha la lunghezza maggiore
def lenMaggiore():
	if len(sottolistaPari)>len(sottolistaDispari):
		print("La lunghezza della sottolista dei numeri pari","(",len(sottolistaPari),")","è maggiore di quella dei numeri dispari","(",len(sottolistaDispari),")\n")
	else:
		print("La lunghezza della sottolista dei numeri dispari","(",len(sottolistaDispari),")","è maggiore di quella dei numeri pari","(",len(sottolistaPari),")\n")

#Funzione per contare le istanze ripetute
def contaRipetizioni():
	j=1
	print("\nEcco le istanze ripetute...\n")
	for i in lista:
		cont=lista.count(i)
		if cont>0:
			print(f"{i:7} {':':2} {'*'*cont}")
			j+=1

N=chiediNumero()
pariDispari()
sommaSottoliste()
lenMaggiore()
contaRipetizioni()
