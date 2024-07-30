#!/bin/bash
#Galesso Federico 3C 16/3/2022 Esercizio in preparazione in verifica
#Creare uno script shell che, chiesto in input all'utente N (compreso tra 3 e 12) permetta di:
# - Caricare il vettore alunni composto di N elementi (cognomi)
# - Caricare il vettore voti composto di N elementi (votazioni), creando numeri random compresi tra 2 e 10
# - Stampare entrambi i vettori
# - Ordinare in modo crescente il vettore cognomi (mantenendo per ogni studente il proprio voto)
# - Creare un terzo vettore contenente solo i voti sufficienti
# - Dato il cognome di un alunno, visualizzare il relativo voto
# - Contare il numero di voti insufficienti

clear

chiediN(){
	echo -n "Inserisci il numero di alunni (3-12): "
	read N
	while [[ $N -lt 3 ]] || [[ $N -gt 12 ]]
	do
		echo -n "Inserisci il numero di alunni (3-12): "
		read N
	done
	return $N
}

declare -a alunni
declare -a voti

caricaAlunni(){
	for (( i=0; i<N; i++ ))
	do
		echo "-- ALUNNO $(( i+1 )) -- "
		echo -n "Inserisci il cognome dell'alunno $(( i+1 )): "
		read  alunni[i]
	done
}

caricaVoti(){
	for (( i=0; i<N; i++ ))
	do
		echo "-- ALUNNO $(( i+1 )) -- "
		echo "Creo il voto random tra 2 e 10"
		creaRandom $1 $2
		voti[i]=$?
	done
}

creaRandom(){
return $(( RANDOM%($2-$1+1)+$1 ))
}

stampaVet(){
	echo "Cognomi: ${alunni[*]}"
	echo "Voti: ${voti[*]}"
}

bubbleSort(){
	N=${alunni[*]}
	J=N
	FLAG=0
	if [[ $FLAG == 0 ]]
	then
		FLAG=1
		for (( i=0; i<10; J-- ))
		do
			if [[ alunni[i] > alunni[i+1] ]]
			then
				TMP=vettore[i]
				alunni[i]=vettore[i+1]
				alunni[i+1]=TMP
				FLAG=0
				$(( J - 1 ))
			fi
		done
	fi
	N=${#alunni[*]}
	echo "Alunni: ${alunni[*]}"
}

chiediN
caricaAlunni
caricaVoti
creaRandom 2 10
stampaVet
bubbleSort
