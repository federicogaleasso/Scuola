#!/bin/bash

#Galeasso Federico 3C 26/1/2022 Esercizio recupero

#Creare uno script che permetta, per un certo numero di persone, di inserire il nome, la statura, il sesso e l'età. Lo script deve inoltre visualizzare un MENU che permetta poi di:
#1. Visualizzare il nome della persona più alta e la relativa statura
#2. Visualizzare la statura media
#3. Visualizzare il nome della persona più giovane e la relativa età
#4. Visualizzare l'età media
#5. Scrivere il numero dei maschi e delle femmine
#6. Scrivere la percentuale dei maschi e delle femmine
#7. Inserire nuovi dati
#8. Uscire dal programma

piu=0
echo -n "Inserisci il numero di persone (>1) --> "
read N
while [[ N -lt 1 ]]
do
	echo -n "Inserisci il numero di persone (>1) --> "
	read N
done
for (( i=0; i<N; i++ ))
do
	piu=$(( piu + 1 ))
	echo -n "Inserisci il nome della persona numero $piu --> "
	read nome
	echo -n "Inserisci l'altezza della persona numero $piu --> "
	read alt
	echo -n "Inserisci il sesso della persona numero $piu (1 m, 0 f) --> "
	read sesso
	if [[ $sesso -ge 1 ]]
	then
		$contm=$(( $contm + 1 ))
	fi
	if [[ $sesso -ge 0 ]]
	then
		$contf=$(( $contf + 1 ))
	fi
	echo -n "Inserisci il'età della persona numero $piu --> "
	read eta
done

errore=5
while [[ errore -eq 5 ]]
do
echo "1 - 2 - 3 - 4 - 5 - 6 - 7 - 8"
read menu
	case $menu in
		1)
			
		;;
		
		2)
		;;
		
		3)
			
		;;
		
		4)
			
		;;
		
		5)
			
		;;
		
		6)
			
		;;
		
		7)
			
		;;
		
		8)
			errore=0
			echo "Ciao ciao!"
		;;
		
		*)
			errore=0
			echo "Menù non valido!"
		;;
	esac
done
