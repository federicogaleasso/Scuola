#!/bin/bash
ContatorePan=0
ContatoreMer=0
Giorno=0
echo -n "Inserisci la quantità di soldi che deve avere Mario: "
read Soldi
while [[ $Soldi -ge 0 ]]
#Giorno=$(( Giorno+1 ))
do
 	echo -n "Cosa vuoi mangiare? 1 per panino (3 euro), 0 per merendina (1 euro): "
 	read Cibo
 		if [[ $Cibo -eq 1 ]]
 		then
 			Soldi=$(( Soldi-3 ))
 			ContatorePan=$(( ContatorePan+1 ))
 		else
 			Soldi=$(( Soldi-1 ))
 			ContatoreMer=$(( ContatoreMer+1 ))
 		fi
done
echo "Hai mangiato $Giorni."
echo "Mario ha mangiato $ContatorePan volte il panino e $ContatoreMer volte la marendina."
