#GALEASSO FEDERICO 4C 28/10/2022 ESERCIZIO IN CLASSE - FUNZIONI CON PASSAGGIO DI PARAMETRI

import os
def clearScreen():
	os.system("clear")
clearScreen()

def aggiungi1(x,z):
	x=x+"Galeasso"
	for i in range(len(z)):
		z[i]+=1

def aggiungi10(y):
	y=y+"Galeasso"
	return y
	
def stampa(x,y,z):
	print(x)
	print(y)	
	print(z)
	
def main():
	a="Federico"
	b="Federico"
	lista=[5,6,7]
	print("Prima: ")
	stampa(a,b,lista)
	aggiungi1(a,lista)
	b=aggiungi10(b)
	print("Dopo: ")
	stampa(a,b,lista)

main()
