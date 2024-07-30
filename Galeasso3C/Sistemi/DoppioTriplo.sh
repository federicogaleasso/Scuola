#!/bin/bash
#Galeasso Federico
#Esercizio
#Dati due numeri, calcolare il doppio e il triplo.
echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
Doppio=$(( N1*2 ))
echo $Doppio
Doppio=$(( N2*2 ))
echo $Doppio
Triplo=$(( N1*3 ))
echo $Triplo
Triplo=$(( N2*3 ))
echo $Triplo
