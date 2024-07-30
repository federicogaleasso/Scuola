#GALEASSO FEDERICO 4C 16/11/2022 COMPITO - BATTAGLIA NAVALE CON I DIZIONARI

#Costruire un campo di battaglia navale (10x10), aggiungendo le coordinate delle navi all'interno di una lista di liste navi [1 nave da 4, 1 nave da 3, 1 nave da 2].
#Ricercare una nave indicandone le coordinate e, se viene trovata, togliere le coordinate dalla lista delle navi ed inserirle in lista di liste navi colpite.
#Segnalare quando viene colpita interamente una delle navi (deve essere cancellata tutta la lista vuota) oppure "mare". Ciclare finchè non vengono colpite tutte le navi

import os

def clearScreen():
	os.system("clear")
clearScreen()

dizNavi = {(1, 1): "Nave colpita!", (1, 2): "Nave colpita!", (1, 3): "Nave colpita!", (1, 4): "Nave colpita!", (5, 2): "Nave colpita!", (5, 3): "Nave colpita!", (5, 4): "Nave colpita!", (3, 7): "Nave colpita!", (3, 8): "Nave colpita!"}

dizNaviColpite = {}

campo = [[0,1,2,3,4,5,6,7,8,9],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

flag=True

print(f"\n{'*'*5} BATTAGLIA NAVALE {'*'*5}\n")

def stampaCampo():
	i=0
	z=0
	for el in campo:
		print(f"{el[0]:2}{el[1]:2}{el[2]:2}{el[3]:2}{el[4]:2}{el[5]:2}{el[6]:2}{el[7]:2}{el[8]:2}{el[9]:2}")
		if i>=1:
			z=z+1
		i=i+1
	print("\n")

def battagliaNavale():
	while flag==True:
		stampaCampo()
		
		riga=int(input("Inserisci la riga (tra 0 e 9): "))
		while riga<0 or riga>9:
			riga=int(input("ERRORE! Inserisci la riga (tra 0 e 9): "))
		
		colonna=int(input("Inserisci la colonna (tra 0 e 9): "))
		while colonna<0 or colonna>9:
			colonna=int(input("ERRORE! Inserisci la colonna (tra 0 e 9): "))
		
		mare=dizNavi.get((riga, colonna), "Mare!")
		print("\n"+mare+"\n")
		
	print("VITTORIA! Hai affondato tutte le navi")
	
battagliaNavale()
