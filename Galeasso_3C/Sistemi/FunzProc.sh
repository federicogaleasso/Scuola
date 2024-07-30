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
