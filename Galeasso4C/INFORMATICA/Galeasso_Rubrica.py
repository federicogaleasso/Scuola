#GALEASSO FEDERICO 4C 26/10/2022 COMPITO 

#Scrivere un programma in Python che permetta di gestire una rubrica telefonica.
#Ogni contatto sarà un elemento della lista e sarà composto da Cognome, Nome, telefono, mail. La struttura della lista sarà quindi una lista con sottoliste composte ognuna da un contatto.
#Progettare un menu che permetta di:
#1. Riempire la rubrica, aggiungendo un elemento alla lista
#2. Cercare un numero di telefono e restituire il cognome e nome del contatto
#3. Dato il cognome, eliminare tutte le informazioni del contatto
#4. Stampare gli elementi della lista
#5. Uscire
#Gestire i casi di errore, di elemento non trovato o lista vuota.

import os
def clearScreen():
	os.system("clear")
clearScreen()

lista=[]
flag=True

print(f"{'*'*5} BENVENUTO {'*'*5}\n")

def riempiLista():
	cognome=input("Inserisci il cognome del contatto --> ")
	while len(cognome)==0:
		cognome=input("Inserisci il cognome del contatto --> ")
	nome=input("Inserisci il nome del contatto --> ")
	while len(nome)==0:
		nome=input("Inserisci il nome del contatto --> ")
	telefono=int(input("Inserisci il telefono del contatto --> "))
	while len(str(telefono))!=10:
		telefono=int(input("Inserisci il telefono del contatto --> "))
	mail=input("Inserisci la mail del contatto --> ")
	while len(mail)==0:
		mail=input("Inserisci la mail del contatto --> ")
	lista.append([cognome,nome,telefono,mail])

def cercaTelefono():
	telefonoTMP=int(input("Inserisci il telefono da cercare --> "))
	while len(str(telefonoTMP))!=10:
		telefonoTMP=int(input("Inserisci il telefono da cercare --> "))
	for list in lista:
		if list[2]==telefonoTMP:
			print("Telefono trovato!")
			print("Cognome:",list[0])
			print("Nome:",list[1])

def eliminaContatto():
	cognomeTMP=input("Inserisci il cognome da cercare --> ")
	for list in lista:
		if list[0]==cognomeTMP:
			print("Cognome trovato!")
			lista.remove(list)

def stampaLista():
	for list in lista:
		print(f"Cognome: {list[0]}\nNome: {list[1]}\nTelefono: {list[2]}\nMail: {list[3]}\n")
	
while flag==True:
	N=int(input("Inserisci un numero da 1 a 4, 5 per uscire --> "))
	if N==1:
		riempiLista()
	if N==2:
		cercaTelefono()
	if N==3:
		eliminaContatto()
	if N==4:
		stampaLista()
	if N==5:
		print("Ciao ciao!")
		flag=False
