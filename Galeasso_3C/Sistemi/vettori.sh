#!/bin/bash

#Galeasso Federico 3C 16/2/2022 Introduzione VETTORI

rapaci=(aquila "falco pellegrino" gufo gheppio barbagianni 12)		#PRIMO metodo per cerare un vettore	#dichiarazione VETTORE, se la parola ha spazi si mette tra virgolette  --> ""

echo "${rapaci[0]}"		#stampa aquila

echo "${rapaci[*]}"		#stampa del vettore

echo "${rapaci[1]}"		#stampa di falco pellegrino

echo "$rapaci"			#stampa il primo, ovvero aquila

dimensione=${#rapaci[*]}	#assegnazione lunghezza del vettore alla variabile dimensione

echo "La dimensione dell'array rapaci è: $dimensione"		#stampa della dimensione del vettore

echo "La dimensione dell'array rapaci è: ${#rapaci[*]}"		#stampa della dimensione del vettore

dim2=${#rapaci[2]}	#assegnazione lunghezza di gufo alla variabile dim2

echo "La dimensione di gufo è $dim2"	#stampa della dimensione dei gufo

dim2=${#rapaci[1]}	#assegnazione lunghezza di falco pellegrino alla variabile dim2

echo "La dimensione di ${rapaci[1]} è $dim2"		#stampa della dimensione dei falco pellegrino

echo "La dimensione di ${rapaci[3]} è ${#rapaci[3]}"		#stampa della dimensione di gheppio

echo "La somma di ${rapaci[1]} e ${rapaci[4]} vale $(( ${#rapaci[1]} + ${#rapaci[4]} ))" #stampa somma dimensione di falco pellegrino e barbagianni

#

rapaci[12]=allocco

echo "${rapaci[*]}" #stampa vettore

echo "La dimensione dell'array rapaci è ${#rapaci[*]}" #stampa somma di tutto il vettore

rapaci[6]=poiana	#cella 6 pioana

echo "${rapaci[*]}"	#stampa vettore, cella 6 pioana

echo "Cosa c'è nella cella 8? ${rapaci[8]}" #nella cella 8 non c'è niente, è nulla

#

a=( ${rapaci[1]} ) #SECONDO metodo per cerare un vettore

echo "${a[0]} ${a[1]}" #stampa di falco, stampa di pellegrino

echo "${a[*]}" #stampa di falco pellegrino

rapaci[8]="piccione brutto e cattivo"

echo "Cosa c'è nella cella 8? ${rapaci[8]}"

#

colori[0]=rosso		#TERZO metodo per cerare un vettore
colori[1]="blu cobalto"
colori[2]="giallo limone"
colori[3]="arcobaleno peppa pig"

echo "${colori[*]}"

echo "La dimensione del vettore \"colori\" è: ${#colori[*]}"

#

declare -a cibo		#QUARTO metodo per creare un vettore, dichiarazione. crea una variabile vuota. con il -a crea un vettore vuoto

for (( i=0;i<5;i++ ))
do
	echo -n "Inserisci il $(( i+1 ))° cibo: "
	read cibo[i]
done

echo "${cibo[*]}"

echo "${cibo[4]}"

#

read -a auto		#QUINTO metodo per creare un vettore
				
echo "${auto[*]}"

#

gatti=([4]=pallino [2]="ciuppi muppi" [0]=alfredo [6]=silvestro)

echo "${gatti[*]}"

unset gatti[4]		#elimina il contenuto della cella 4, ovvero pallino

echo "Ho cancellato il contenuto della cella 4"

echo "${gatti[*]}"

unset gatti		#elimina il contenuto del vettore

echo "${gatti[*]}"

echo "Ho cancellato il vettore"
