#!/bin/bash
#Script
#Galeasso Federico 3C 12/10/2021
cd ~/Scrivania
mkdir Esercizio
cd Esercizio/
mkdir Corrisponden
cd Corrisponden/
mkdir Amici
mkdir Conoscenti
mkdir Parenti
cd Amici
mkdir Mare
mkdir Montagna
mkdir Città
mkdir Lago
cd Mare
mkdir Livorno
mkdir Genova
mkdir Rimini
mkdir Messina
cd ..
cd Montagna
mkdir Aosta
mkdir Stroppo
mkdir Livigno
cd ..
cd Città
mkdir Torino
mkdir Roma
cd ..
cd Lago
mkdir Como
mkdir Verbiana
cd ..
cd ..
cd Conoscenti
mkdir Mare
mkdir Montagna
mkdir Città
mkdir Lago
cd Mare
mkdir Livorno
mkdir Genova
mkdir Rimini
mkdir Messina
cd ..
cd Montagna
mkdir Aosta
mkdir Stroppo
mkdir Livigno
cd ..
cd Città
mkdir Torino
mkdir Roma
cd ..
cd Lago
mkdir Como
mkdir Verbiana
cd ..
cd ..
cd Parenti
mkdir Nonni
mkdir Zii
mkdir Cugini
cd ..
cd Conoscenti
cd Montagna
cd Stroppo
touch elencoAmici.txt
echo "Federico, Alessandro, Francesco, Mattia">elencoAmici.txt
cp elencoAmici.txt ~/Scrivania/Esercizio/Corrisponden/Amici/Montagna/Stroppo
echo "Massimo, Nicolò, Paolo, Lorenzo">>elencoAmici.txt
mv ~/Scrivania/Esercizio/Corrisponden/Amici/Montagna/Stroppo/elencoAmici.txt ~/Scrivania/Esercizio/Corrisponden/Amici/Montagna/Stroppo/elencoAmiciAmici.txt
mv ~/Scrivania/Esercizio/Corrisponden/Conoscenti/Montagna/Stroppo/elencoAmici.txt ~/Scrivania/Esercizio/Corrisponden/Conoscenti/Montagna/Stroppo/elencoAmiciAmici.txt
cd ..
cd ..
cd Lago
cd Como
touch inutile.txt
cd ..
cd ..
rm -rf Lago
cd ..
cd Parenti
cd Cugini
touch indirizzi.txt
echo "Moretta, Torino, Cuneo, Saluzzo">indirizzi.txt
cp indirizzi.txt ~/Scrivania/Esercizio/Corrisponden/Parenti/Nonni
echo "Savigliano, Manta, Verzuolo, Pinerolo">indirizzi.txt
cat ~/Scrivania/Esercizio/Corrisponden/Parenti/Cugini/indirizzi.txt ~/Scrivania/Esercizio/Corrisponden/Parenti/Nonni/indirizzi.txt>~/Scrivania/Esercizio/Corrisponden/Parenti/indirizzi.txt
cat ~/Scrivania/Esercizio/Corrisponden/Parenti/indirizzi.txt
cd ..
ls -laRX
