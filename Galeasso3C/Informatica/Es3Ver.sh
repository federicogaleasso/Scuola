#!/bin/bash
echo -n "Inserisci il nome della prima persona: "
read primo
echo -n "Inserisci il nome della seconda persona: "
read secondo
echo -n "Inserisci il nome della terza persona: "
read terzo
echo -n "Inserisci il nome della quarta persona: "
read quarto
echo -n "Inserisci l'età della prima persona: "
read primoeta
echo -n "Inserisci l'età della seconda persona: "
read secondoeta
echo -n "Inserisci l'età della terza persona: "
read terzoeta
echo -n "Inserisci l'età della quarta persona: "
read quartoeta
echo -n "Prima, Inserisci 0 se è maschio, 1 se è femmina: "
read primosesso
echo -n "Seconda, Inserisci 0 se è maschio, 1 se è femmina: "
read secondosesso
echo -n "Terza, Inserisci 0 se è maschio, 1 se è femmina: "
read terzosesso
echo -n "Quarta, Inserisci 0 se è maschio, 1 se è femmina: "
read quartosesso
if [[ primosesso -eq 1 ]]
then
echo "la prima persona è femmina"
fi
if [[ secondosesso -eq 1 ]]
then
echo "la seconda persona è femmina"
fi
if [[ terzosesso -eq 1 ]]
then
echo "la terza persona è femmina"
fi
if [[ quartosesso -eq 1 ]]
then
echo "la quarta persona è femmina"
fi
