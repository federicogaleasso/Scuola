#!/bin/bash

#Galeasso Federico 3C 7/2/2022 Esercizio in preprazione alla verifica

#“La Morra Cinese”
#Scrivere uno script shell che permetta di giocare al gioco della Morra Cinese contro il computer.
#Lo script deve visualizzare un MENU di gioco con le seguenti voci:
#1. Nuova partita
#2. Statistiche
#3. Esci
#La voce n.1 permette di giocare un numero N di round. - N è generato in maniera casuale (utilizzando una funzione "CreaNumero") ed è compreso tra 3 e 8.- L'utente ed il computer effettuano una mossa per volta e la prima mossa è sempre dell'utente.- Ad ogni turno dell'utente, lo script visualizza un menù con le mosse possibili che sono:   c. carta  f. forbice  s. sasso
#Le mosse del PC devono essere generate in maniera casuale (utilizzando la funzione "CreaNumero")con valori compresi tra 1 e 3, dove: 1. carta 2. forbice 3. sasso
#Inoltre, le mosse del PC devono essere sempre stampate a video (carta, forbice o sasso). Ad ogni turno, il vincitore è stabilito in questo modo:- carta vince su sasso, ma perde su forbice- forbice vince su carta, ma perde su sasso- sasso vince su forbice, ma perde su carta
#Il punteggio totale di ogni partita è stabilito sommando i punteggi parziali ad ogni round:1 punto per la vittoria, 0 per il pareggio
#La voce n.2 permette di visualizzare le statistiche di tutte le partite giocate, ovvero:- N° totale di partite giocate- N° di partite vinte contro il PC- N° di partite perse contro il PC
#La voce n.3 permette all'utente di uscire dal gioco dopo aver chiesto la conferma.

clear

uno(){
	clear
	pgiocate=$(( pgiocate + 1 ))
	piu=0
	(( N=RANDOM %6+3 ))
	echo "Sei pronto? giocherai $N round. Premi invio per continuare..."
	read
	clear
	for (( i=0; i<N; i++ ))
	do
		piu=$(( piu+1 ))
		echo " ____________________________________________________"
		echo "|            Questo è il $piu° ROUND		     |"
		echo "|____________________________________________________|"
		echo " "
		echo "Tocca a TE"
		echo " "
		echo "Premi 1 per CARTA, 2 per FORBICE e 3 per SASSO"
		echo " "
		read cfs
		if [[ $cfs -eq 1 ]]
		then
		echo " "
			echo "CARTA"
		fi
		if [[ $cfs -eq 2 ]]
		then
		echo " "
			echo "FORBICE"
		fi
		if [[ $cfs -eq 3 ]]
		then
		echo " "
			echo "SASSO"
		fi
		echo " "
		echo "E' il turno del PC"
		echo " "
		(( nPc=RANDOM %3+4 ))
		if [[ $nPc -eq 4 ]]
		then
			echo " "
			echo "Il PC ha scelto CARTA"
			echo " "
		fi
		if [[ $nPc -eq 5 ]]
		then
		 	echo " "
			echo "Il PC ha scelto FORBICE"
			echo " "
		fi
		if [[ $nPc -eq 6 ]]
		then
		 	echo " "
			echo "Il PC ha scelto SASSO"
			echo " "
		fi
		if [[ cfs -eq 1 ]] && [[ nPc -eq 4 ]] #carta carta
		then
			echo "Pareggio"
			contpar=$(( contpar+1 ))
		fi
		if [[ cfs -eq 2 ]] && [[ nPc -eq 5 ]] #forbice forbice
		then
			echo "Pareggio"
			contpar=$(( contpar+1 ))
		fi
		if [[ cfs -eq 3 ]] && [[ nPc -eq 6 ]] #sasso sasso
		then
			echo "Pareggio"
			contpar=$(( contpar+1 ))
		fi
		#*******************************************
		if [[ cfs -eq 1 ]] && [[ nPc -eq 5 ]] #carta forbice
		then
			echo "Hai perso"
			contpers=$(( contpers+1 ))
		fi
		
		if [[ cfs -eq 1 ]] && [[ nPc -eq 6 ]] #carta sasso
		then
			echo "Hai vinto"
			contvitt=$(( contvitt+1 ))
		fi
		#*******************************************
		if [[ cfs -eq 2 ]] && [[ nPc -eq 4 ]] #forbice carta
		then
			echo "Hai vinto"
			contvitt=$(( contvitt+1 ))
		fi
		
		if [[ cfs -eq 2 ]] && [[ nPc -eq 6 ]] #forbice sasso
		then
			echo "Hai perso"
			contpers=$(( contpers+1 ))
		fi
		#*******************************************
		if [[ cfs -eq 3 ]] && [[ nPc -eq 4 ]] #sasso carta
		then
			echo "Hai vinto"
			contvitt=$(( contvitt+1 ))
		fi
		
		if [[ cfs -eq 3 ]] && [[ nPc -eq 5 ]] #sasso forbice
		then
			echo "Hai perso"
			contpers=$(( contpers+1 ))
		fi
		echo " "
		echo "Premi invio per continuare..."
		read
		clear
	done
}

errore=5
while [[ errore -eq 5 ]]
do
	clear
	echo " ____________________________________________________"
	echo "|          MORRA CINESE - OPZIONI DISPONIBI          |"
	echo "|____________________________________________________|"
	echo "| 1 - Nuova partita                                  |"
	echo "| 2 - Statistiche                                    |"
	echo "| 3 - EXIT                                           |"
	echo "|____________________________________________________|"
	echo -n "Inserire una scelta: "
	read menu
	case $menu in
		1)
			uno
		;;
		
		2)
			clear
			echo " ____________________________________________________"
			echo "|            MORRA CINESE - STATISTICHE              |"
			echo "|____________________________________________________|"
			echo "Partite giocate: $pgiocate"
			echo "Vinte: $contvitt"
			echo "Perse: $contpers"
			echo "Pareggiate: $contpar"
			echo "Premi invio per continuare..."
			read
			clear
		;;
		
		3)
			echo "Sei sicuro di voler uscire? [y/n]"
			read exit
			if [[ $exit == 'y' ]] || [[ $exit == 'Y' ]]
			then
				echo "Ciao!"
				errore=0
			fi
		;;
		*)
			echo "Menù non valido!"
		;;
	esac
done
