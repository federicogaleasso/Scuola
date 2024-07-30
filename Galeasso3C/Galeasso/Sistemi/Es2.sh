#!/bin/bash
cd ~/Scrivania
mkdir Esercizio2
cd Esercizio2
Numero=10
echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
echo -n "Inserisci il terzo numero: "
read N3
echo -n "Inserisci il quarto numero: "
read N4
Somma1=$(( N1 + N2 + N3 + N4 ))
echo $Somma1
if [[ $N1$N2$N3$N4 -lt $Numero ]]
then
 Somma2=$(( N1 + N2 + N3 + N4 ))
echo $Somma2
fi
if [[ $N1$N2$N3$N4 -ge $Numero ]]
then
	Molt3=$(( N1 * N2 * N3 * N4 ))
echo $Molt3
fi
echo $Somma1 $Somma2 $Somma3 > totali.txt
more totali.txt
