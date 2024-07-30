#!/bin/bash
#Presentare all'utente un menù di scelta
# 0 --> Esci
# 1 --> Somma N numeri random da 4 a 20, con N chiesto all'utente
# 2 --> Differenza di due numeri chiesti all'utente
# 3 --> Prodotto di N numeri random da 8 a 15, N chiesto all'utente
# 4 --> Divisione di due numeri chiesti all'utente

echo "Questo è il menù di scelta:
0 --> Esci
1 --> Somma N numeri random da 4 a 20, con N chiesto all'utente
2 --> Differenza di due numeri chiesti all'utente
3 --> Prodotto di N numeri random da 8 a 15, N chiesto all'utente
4 --> Divisione di due numeri chiesti all'utente"
read Menu
case $Menu in
	0) echo "Programma terminato!" ;;
	
	1) echo -n "Quanti numeri vuoi sommare? "
		read N
		for (( i=0; i<N; i++ ))
			do
				(( i=RANDOM %17+4 ))
			done
		echo "$i"
	;;
	
	2) echo -n "Inserisci il primo numero:  "
		read N1
		echo -n "Inserisci il secondo numero:  "
		read N2
		Sottrazione=$(( N1-N2 ))
		echo "La sottrazione tra $N1 e $N2 vale $Sottrazione"
	;;
	
	3) echo -n "Quanti numeri vuoi moltiplicare? "
		read N
		for (( i=0; i<N; i++ ))
			do
				(( i=RANDOM %8+8 ))
			done
		echo "$i"
	;;
	
	4) echo -n "Inserisci il primo numero:  "
		read N1
		echo -n "Inserisci il secondo numero:  "
		read N2
		Divisione=$(( N1/N2 ))
		echo "La sottrazione tra $N1 e $N2 vale $Divisione"
	;;
	
	*) echo "Menù non valido!" ;;
esac
