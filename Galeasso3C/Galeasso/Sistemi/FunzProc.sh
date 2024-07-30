#Gleasso Federico 3C 22/12/2021 Funzioni e Procedure

#!/bin/bash

function Saluto {
	echo -n "Come ti chiami? --> "
	read  Nome
	echo "Ciao $Nome"	
}

sommaValori(){
	echo -n "Inserisci il primo valore: "
	read  N1
	echo -n "Inserisci il secondo valore: "
	read  N2
	Somma=$(( N1 + N2 ))
	echo "La somma vale --> $Somma"
}

moltiplica(){
	local molt=1
	for (( i=0; i<5; i++ ))
	do
		echo -n "Inserisci un valore: "
		read N
		molt=$(( molt*N ))
	done
return $molt
}

Saluto
sommaValori
moltiplica
m=$?
echo "Il risultato della moltiplicazione vale --> $m"

#ESERCIZIO

#Visualizza un menù all'utente con le voci

# + --> SOMMA
# - --> SOTTRAI
# X --> MOLTIPLICA
# : --> DIVIDI
# E --> EXIT

# Ogni voce del menù deve richiamare una funzione che chiede  all'utente di inserire N numeri e restituire il risultato delle relative operazioni (Per la divisione solo due numeri - valutare il caso della divisione per zero).

SOMMA() {
		echo -n "Inserisci il numero di numeri che vuoi inserire: "
		read Numeri
		for (( i=0; i<Numeri; i++ ))
		do
			echo -n "Inserisci il numero: "
			read  N
		done
		Som=$(( Som + N ))
return $Som
}

echo "Scegli una voce del seguente menù"
echo -n "+ --> SOMMA
- --> SOTTRAI
X --> MOLTIPLICA
: --> DIVIDI
E --> EXIT
La tua scelta --> "
read Menu

case $Menu in
	"+")
		SOMMA
		s=$?
		echo "La somma vale $s"
	;;
esac
