#!/bin/bash

#Galeasso Federico 3C 25/11/2021 Esercizio

#Realizzare uno script che:

#Richieda all’utente 4 numeri;
#Richieda all’utente 2 stringhe;

#Visualizzi il seguente menu:
#Premi A per la somma dei 4 numeri;
#Premi B per la media dei 4 numeri;
#Premi C per visualizzare il maggiore dei 4 numeri;
#Premi D per visualizzare il minore dei 4 numeri;
#Premi E per confrontare se le stringhe sono uguali;
#Premi F per verificare se i 4 numeri sono uguali;
#Premi G per stampare le stringhe in ordine alfabetico;
#Premi H per verificare se le stringhe sono vuote;
#Premi R per richiedere nuovamente l'inserimento dei 4 numeri e delle stringhe;
#Premi Z per uscire.

#Lo script deve fornire una risposta ad ogni voce di menu

Risultato=0

echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
echo -n "Inserisci il terzo numero: "
read N3
echo -n "Inserisci il quarto numero: "
read N4

echo -n "Inserisci l'iniziale del tuo nome: "
read Nome
echo -n "Inserisci l'iniziale del tuo cognome: "
read Cognome

echo "Visualizzi il seguente menu:
Premi A per la somma dei 4 numeri;
Premi B per la media dei 4 numeri;
Premi C per visualizzare il maggiore dei 4 numeri;
Premi D per visualizzare il minore dei 4 numeri;
Premi E per confrontare se le stringhe sono uguali;
Premi F per verificare se i 4 numeri sono uguali;
Premi G per stampare le stringhe in ordine alfabetico;
Premi H per verificare se le stringhe sono vuote;
Premi R per richiedere nuovamente l'inserimento dei 4 numeri e delle stringhe;
Premi Z per uscire."
read Menu

case $Menu in
	A | a) Risultato=$(( N1 + N2 + N3 + N4 )) 
		echo "$Risultato"
	;;
	B | b) Risultato=$(( (N1 + N2 + N3 + N4)/4 ))
		echo "$Risultato"
	;;
	C | c) if [[ $N1 -gt $N2 ]]
		then
			if [[ $N1 -gt $N3 ]]
			then
				if [[ $N1 -gt $N4 ]]
				then
					echo "$N1"
				else
					echo "$N4"
				fi
			else
				echo "$N3"
			fi
		else
			if [[ $N2 -gt $N4 ]]
			then
				if [[ $N2 -gt $N3 ]]
				then
					echo "$N2"
				else
					echo "$N3"
				fi
			else
				echo "$N4"
			fi
		fi
	
	;;
	D | d)	if [[ $N1 -lt $N2 ]]
		then
			if [[ $N1 -lt $N3 ]]
			then
				if [[ $N1 -lt $N4 ]]
				then
					echo "$N1"
				else
					echo "$N4"
				fi
			else
				echo "$N3"
			fi
		else
			if [[ $N2 -lt $N4 ]]
			then
				if [[ $N2 -lt $N3 ]]
				then
					echo "$N2"
				else
					echo "$N3"
				fi
			else
				echo "$N4"
			fi
		fi
	
	;;

	E | e) if [[ $Nome = $Cognome ]]
		then
			echo "Le due stringhe sono uguali"
		else
			echo "Le due stringhe sono diverse"
		fi
	
	;;
	F | f)	if [[ $N1 -eq $N4 ]] && [[ $N2 -eq $N3 ]] && [[ $N3 -eq $N1 ]] && [[ $N1 -eq $N4 ]] && [[ $N2 -eq $N4 ]] && [[ $N3 -eq $N4 ]]
		then
			echo "I 4 numeri sono uguali"
		else
			echo "I 4 numeri sono diversi"
		fi
	
	;;
	G | g)	if [[ $Nome > $Cognome ]]
		then
			echo "$Cognome	$Nome"
		else
			echo "$Nome	$Cognome"
		fi

	
	;;
	H | h)	if [[ -z $Nome ]]
		then 
			echo "La prima stringa è vuota"
		else
			echo "La prima stringa è piena"
		fi
		if [[ -z $Cognome ]]
		then 
			echo "La seconda stringa è vuota"
		else
			echo "La seconda stringa è piena"
		fi
	
	;;
	R | r) Risultato=0

echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
echo -n "Inserisci il terzo numero: "
read N3
echo -n "Inserisci il quarto numero: "
read N4

echo -n "Inserisci l'iniziale del tuo nome: "
read Nome
echo -n "Inserisci l'iniziale del tuo cognome: "
read Cognome

echo "Visualizzi il seguente menu:
Premi A per la somma dei 4 numeri;
Premi B per la media dei 4 numeri;
Premi C per visualizzare il maggiore dei 4 numeri;
Premi D per visualizzare il minore dei 4 numeri;
Premi E per confrontare se le stringhe sono uguali;
Premi F per verificare se i 4 numeri sono uguali;
Premi G per stampare le stringhe in ordine alfabetico;
Premi H per verificare se le stringhe sono vuote;
Premi R per richiedere nuovamente l'inserimento dei 4 numeri e delle stringhe;
Premi Z per uscire."
read Menu

case $Menu in
	A) Risultato=$(( N1 + N2 + N3 + N4 )) 
		echo "$Risultato"
	;;
	B) Risultato=$(( (N1 + N2 + N3 + N4)/4 ))
		echo "$Risultato"
	;;
	C) if [[ $N1 -gt $N2 ]]
		then
			if [[ $N1 -gt $N3 ]]
			then
				if [[ $N1 -gt $N4 ]]
				then
					echo "$N1"
				else
					echo "$N4"
				fi
			else
				echo "$N3"
			fi
		else
			if [[ $N2 -gt $N4 ]]
			then
				if [[ $N2 -gt $N3 ]]
				then
					echo "$N2"
				else
					echo "$N3"
				fi
			else
				echo "$N4"
			fi
		fi
	
	;;
	D)	if [[ $N1 -lt $N2 ]]
		then
			if [[ $N1 -lt $N3 ]]
			then
				if [[ $N1 -lt $N4 ]]
				then
					echo "$N1"
				else
					echo "$N4"
				fi
			else
				echo "$N3"
			fi
		else
			if [[ $N2 -lt $N4 ]]
			then
				if [[ $N2 -lt $N3 ]]
				then
					echo "$N2"
				else
					echo "$N3"
				fi
			else
				echo "$N4"
			fi
		fi
	
	;;

	E) if [[ $Nome = $Cognome ]]
		then
			echo "Le due stringhe sono uguali"
		else
			echo "Le due stringhe sono diverse"
		fi
	
	;;
	F)	if [[ $N1 -eq $N4 ]] && [[ $N2 -eq $N3 ]] && [[ $N3 -eq $N1 ]] && [[ $N1 -eq $N4 ]] && [[ $N2 -eq $N4 ]] && [[ $N3 -eq $N4 ]]
		then
			echo "I 4 numeri sono uguali"
		else
			echo "I 4 numeri sono diversi"
		fi
	
	;;
	G)	if [[ $Nome > $Cognome ]]
		then
			echo "$Cognome	$Nome"
		else
			echo "$Nome	$Cognome"
		fi

	
	;;
	H)	if [[ -z $Nome ]]
		then 
			echo "La prima stringa è vuota"
		else
			echo "La prima stringa è piena"
		fi
		if [[ -z $Cognome ]]
		then 
			echo "La seconda stringa è vuota"
		else
			echo "La seconda stringa è piena"
		fi
	;;
	Z)
		echo "Programma terminato!"
	;;
esac
	
	;;
	Z | z)
		echo "Programma terminato!"
	;;
	*) echo "Lettera non valida!" ;;
esac
