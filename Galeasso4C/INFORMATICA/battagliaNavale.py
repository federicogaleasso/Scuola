#GALEASSO FEDERICO 4C 19/10/2022 COMPITO BATTAGLIA NAVALE

#Costruire un campo di battaglia navale (10x10), aggiungendo le coordinate delle navi all'interno di una lista di liste navi [1 nave da 4, 1 nave da 3, 1 nave da 2].
#Ricercare una nave indicandone le coordinate e, se viene trovata, togliere le coordinate dalla lista delle navi ed inserirle in lista di liste navi colpite.
#Segnalare quando viene colpita interamente una delle navi (deve essere cancellata tutta la lista vuota) oppure "mare". Ciclare finchè non vengono colpite tutte le navi

import os
def clearScreen():
	os.system("clear")
clearScreen()

Campo = [[0,1,2,3,4,5,6,7,8,9],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
navi=[[2],[1],[4],[1,2,3,4],[7,8,9],[5,6]]
navicolpite=[]

print(f"\n{'*'*5} BATTAGLIA NAVALE {'*'*5}\n")

def stampaCampo():
	i=0
	z=0
	for el in Campo:
		print(f"{z:5}{el[0]:8}{el[1]:8}{el[2]:8}{el[3]:8}{el[4]:8}{el[5]:8}{el[6]:8}{el[7]:8}{el[8]:8}{el[9]:8}")
		if i>=1:
			z=z+1
		i=i+1
		print("\n")

stampaCampo()

X=int(input("Coordinata X (tra 0 e 9) --> "))
while X>9 or X<0:
	X=int(input("ERRORE! Coordinata X (tra 0 e 9) --> "))
Y=int(input("Coordinata Y (tra 0 e 9) --> "))
while Y>9 or Y<0:
	Y=int(input("ERRORE! Coordinata Y (tra 0 e 9) --> "))
print("\n")

stampaCampo()
