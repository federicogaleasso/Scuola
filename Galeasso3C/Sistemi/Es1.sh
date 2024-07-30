#!/bin/bash
cd ~/Scrivania
mkdir Esercizio1
touch Uno.txt
echo -n "Inserisci un parola: "
read ParolaUno
echo $ParolaUno > Uno.txt
touch Due.txt
echo -n "Inserisci un parola: "
read ParolaDue
echo $ParolaDue > Due.txt
touch Tre.txt
echo -n "Inserisci un parola: "
read ParolaTre
echo $ParolaTre > Tre.txt
cp Uno.txt Due.txt Tre.txt ~/Scrivania/Esercizio1
cat Uno.txt Due.txt Tre.txt > unione.txt
more unione.txt
cd ~/Scrivania
rm Uno.txt Due.txt Tre.txt
echo "Inserisci il tuo nome"
read Nome
echo "Inserisci il tuo cognome"
read Cognome
echo "Inserisci la tua classe"
read Classe
echo $ParolaUno $ParolaDue $ParolaTre $Nome $Cognome $Classe > unione.txt
more unione.txt
ls Esercizio1
