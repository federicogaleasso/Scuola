#!/bin/bash

for (( i=0; i<10; i++ )) #sintassi FOR
do
	echo "$i"
done

#esercizio

Lettera=a

while [[ $Lettera != "F" ]]
do
	echo -n "Inserisci una lettera (F per terminare): "
	read Lettera

	case $Lettera in #sintassi SWITCH
		A)
			echo "Vocale A"
		;;
		
		E)
			echo "Vocale E"
		;;
		
		I)
			echo "Vocale I"
		;;
		
		O)
			echo "Vocale O"
		;;
		
		U)
			echo "Vocale U"
		;;
		
		F)
			echo "Hai scelto di uscire!"
		;;
		
		*)
		echo "Consonante"
		;;
	esac
done

#Operatori tra stringhe
# s1 = s2 (confronta se sono uguali)
# s1 != s2 (confronta se sono diversi)
# s1 < s2 (confronta se s1 è minore alfabeticamente di s2)
# s1 > s2 (confronta se s1 è maggiore alfabeticamente di s2)
# -n s2 (controlla che s1 NON SIA vuota)
# -z s2 (controlla che s1 SIA vuota)

Password1="FEDE"
while [[ -n $Password1 ]]
do
	echo "Inserisci la tua password: "
	read Password1
	echo "Devo controllare la password. Reinseriscila: "
	read Password2
	if [[ $Password1 = $Password2 ]]
	then
		echo "Password accettata"
		Password1=""
	else
		echo "Le due password non coincidono."
	fi
done

(( N1=RANDOM %11 ))
echo "$N1"

if [[ condizione1 ]] || [[ condizione2 ]] && [[ condizione3 ]]
