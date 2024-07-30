#GALEASSO FEDERICO 4C 5/10/2022 COMPITO CAMBIO EURO/DOLLARI

import os
def clearScreen():
	os.system("clear")
clearScreen()

euro=float(input("Inserisci l'importo in euro (>0) --> "))
while euro <= 0:
	euro=float(input("ERRORE! Inserisci l'importo in euro (>0) --> "))
cambio=float(input("Inserisci il cambio euro/dollaro (>0) --> "))
while cambio <= 0:
	cambio=float(input("ERRORE! Inserisci il cambio euro/dollaro (>0) --> "))
dollari=euro*cambio
print('\n{0:^20} {1:^20} {2:^20}' .format("Euro", "Cambio", "Dollari"))
print('{0:^20.2f} {1:^20.2f} {2:^20.2f}' .format(euro, cambio, dollari))
