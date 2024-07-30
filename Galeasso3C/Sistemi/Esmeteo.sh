#Creare uno script di shell per una stazione meteorologica che ha la necessità di controllare le temperature delle città. Il programma deve visualizzare all'utente un menu con le seguenti voci:
#A: Inserisci temperature B: Medie temperature C: Temperature MAX e MIN D: ESCI Ogni singola voce del menu ha il seguente comportamento:
#A --> Richiama una funzione "Inserimento" che permette all'utente di inserire il nome della città, la temperaturaminima registrata (valore compreso tra -5 e 8) e la temperatura massima registrata (valore compreso tra 5 e 23);
#B --> Richiama una funzione "ValoriMedi" che permette di visualizzare i seguenti valori:  1. La media di tutte le temperature inserite  2. La media delle temperature massime  3. La media delle temperature minimeNB: Per il calcolo dei valore delle medie, utilizzare un'apposita funzione "media" a cui passare i parametri opportuni (ad. esempio la somma delle temperature massime ed il numero di tali temperature);
#C --> Visualizza i valori di temperatura max e min registrati con i corrispondenti nomi delle città.D --> Permette di terminare il programma.

#!/bin/bash

Inserimento(){
	echo -n "Inserisci il nome della città --> "
	read citta
	echo -n "Inserisci la temperatura minima (tra -5 e 8) --> "
	read min
	if [[ $min -lt -5 ]] || [[ $min -gt 8 ]]
	then
		echo -n "Inserisci la temperatura minima (tra -5 e 8) --> "
		read min
	fi
	echo -n "Inserisci la temperatura massima (tra 5 e 23) --> "
	read max
	if [[ $min -lt 5 ]] || [[ $min -gt 23 ]]
	then
		echo -n "Inserisci la temperatura massima (tra 5 e 23) --> "
		read max
	fi
}

echo -n "A - B - C - D --> "
read Menu

case $Menu in
	'A')
		Inserimento
	;; 
esac
