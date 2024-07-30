#!/bin/bash
echo -n "Come ti chiami? " #printf in c
read NomeUtente #scanf in c
echo "Ciao $NomeUtente, benvenuto!"
Parola="A B C					D"
echo $Parola # NON mette gli spazi
echo "$Parola" #mette gli spazi
a=12
echo "La variabile a vale $a"
Somma=7+5
echo $Somma
N1=7
N2=5
Somma=$(( N1+N2 )) #ci va lo spazio
echo $Somma

#Condizioni
#Dati due numeri, stabilire se sono uguali o diversi.
echo -n "Inserisci il primo numero: "
read N1
echo -n "Inserisci il secondo numero: "
read N2
if [[ $N1 -eq $N2 ]] #condizione
then #per aprire if --> in C: {
	echo "I due numeri sono uguali"
else
	echo "I numeri sono diversi"
fi #per chiudere if,  scrivi if al contrario --> in C: }

#OPERATORI
# -eq verifica se sono UGUALI
# -ne verifica se sono DIVERSI
# -gt MAGGIORE DI
# -ge MAGGIORE UGUALE
# -lt MINORE DI
# -le MINORE UGUALE

# elif sta per else e if insieme
