#!/bin/bash

#Galeasso Federico 3C 2/3/2022 Vettore Bubble Sort

vettore=(10 9 20 24 2 44 7 8 9 18)
echo "${vettore[*]}"
N=${vettore[*]}
J=N
FLAG=0
if [[ $FLAG == 0 ]]
then
	FLAG=1
	for (( i=0; i<10; J-- ))
	do
		if [[ vettore[i] > vettore[i+1] ]]
		then
			TMP=vettore[i]
			vettore[i]=vettore[i+1]
			vettore[i+1]=TMP
			FLAG=0
			$(( J - 1 ))
		fi
	done
fi
N=${#vettore[*]}
