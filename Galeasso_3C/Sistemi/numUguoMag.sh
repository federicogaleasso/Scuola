#!/bin/bash
#Galeasso Federico
#Esercizio
#Dati due numeri stabilire se sono uguali e, in caso contrario stabilire il maggiore.
echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
if [[ $N1 -eq $N2 ]]
then
	echo "I due numeri sono uguali"
elif [[ $N1 -gt $N2 ]]
then
	echo "Il numero $N1 è maggiore di $N2"
else
	echo "Il numero $N2 è maggiore di $N1"
fi
