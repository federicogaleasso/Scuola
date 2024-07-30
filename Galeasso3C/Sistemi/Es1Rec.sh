#!/bin/bash

#Galeasso Federico 3C 26/1/2022 Esercizio recupero
#Scrivere un programma che presenti all’utente il seguente menu di scelta, da riproporre finché non viene selezionata la quarta voce:
#1. Perimetro
#2. MediaMaggiore
#3. Quanti
#4. Esci
#La voce 1 richiama una funzione che chiede all’utente di inserire il numero dei lati e la misura di ciascun lato di un poligono regolare, calcola il perimetro e lo visualizza in output. Se il numero di lati non è consono, visualizza la scritta “Poligono non previsto”.
#La voce 2 richiama una funzione che chiede all’utente di inserire N numeri interi, calcola la media dei numeri pari, la media dei numeri dispari (utilizzando una funzione calcolaMedia a cui vengono passati come parametri la somma ed il numero di elementi opportuno), le confronti e visualizzi in output la maggiore delle due.
#La voce 3 richiama una funzione che chiede all’utente di inserire le altezze di alcuni studenti e studentesse (l'inserimento termina premendo 0), conta quanti superano l'altezza "standard" 170cm. Visualizza in output il numero totale degli studenti e studentesse, il numero di quanti superano l'altezza standard, il numero totale di studentesse ed il numero totale di studenti.
#La voce 4 saluta l'utente e chiude il programma.

perimetro(){
	echo -n "Inserisci il numero dei lati (numero lati >2 e <10) --> "
	read  nLati
	while [[ nLati -lt 3 ]] || [[ nLati -gt 9 ]]
	do
		echo -n "Poligono non previsto! Inserisci il numero dei lati (numero lati >2 e <10) --> "
		read  nLati
	done
	echo -n "Inserisci la misura dei lati (misura >0) --> "
	read misura
	while [[ misura -le 0 ]]
	do
		echo -n "Inserisci la misura dei lati (misura >0) --> "
		read misura
	done
	per=$(( misura * nLati ))
	echo "$per"
}

piu=0
quanti(){
	num=3
	while [[ num -ne 0 ]]
	do
		echo -n "Insersci 1 per studenti, 2 per studentesse, 0 per terminare --> "
		read num
		if [[ num -eq 1 ]]
		then
			echo -n "Inserisci il numero di studenti a cui vuoi chiedere l'altezza (>1) --> "
			read nM
			while [[ nM -lt 1 ]]
			do
				echo -n "Inserisci il numero di studenti a cui vuoi chiedere l'altezza (>1) --> "
				read nM
			done
			for (( i=0; i<nM; i++ ))
			do
				piu=$(( piu + 1 ))
				echo -n "Inserisci l'altezza dello studente numero $piu --> "
				read altM
				if [[ altM -gt 170 ]]
				then
					contAltM=$(( contAltM + 1 ))
				fi
			done
		fi

		if [[ num -eq 2 ]]
		then
			echo -n "Inserisci il numero di studentesse a cui vuoi chiedere l'altezza (>1) --> "
			read nF
			while [[ nF -lt 1 ]]
			do
				echo -n "Inserisci il numero di studentesse a cui vuoi chiedere l'altezza (>1) --> "
				read nF
			done
			for (( i=0; i<nF; i++ ))
			do
				piu=$(( piu + 1 ))
				echo -n "Inserisci l'altezza della studentessa numero $piu --> "
				read altF
				if [[ altF -gt 170 ]]
				then
					contAltF=$(( contAltF + 1 ))
				fi
			done
		fi
	done
	echo "Gli studenti che superano l'altezza standard (170cm) sono $contAltM"
	echo "Le studentesse che superano l'altezza standard (170cm) sono $contAltF"
}

errore=5
while [[ errore -eq 5 ]]
do
echo "Questo è il menù di scelta:
1 --> Perimetro
2 --> MediaMaggiore
3 --> Quanti
4 --> Esci"
read menu
	case $menu in
		1)
			perimetro
		;;
		
		2)
		;;
		
		3)
			quanti
		;;
		
		4)
			errore=0
			echo "Ciao ciao!"
		;;
		
		*)
			errore=0
			echo "Menù non valido!"
		;;
	esac
done
