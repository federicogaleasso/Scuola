def mediaPrezziQuantita(quantitaTot,prezzoTot,n):
	mediaPrezzi=0
	mediaQuantita=0
	mediaPrezzi=prezzoTot/n
	mediaQuantita=quantitaTot/n
	print(f"\nIl prezzo medio è: {mediaPrezzi}")
	print(f"La quantità media è: {mediaQuantita}")

def venditeTotali(quantitaTot,prezzoTot):
	venditeTot=0
	venditeTot=prezzoTot*quantitaTot
	print(f"Il valore totale delle vendite è: {venditeTot}")
