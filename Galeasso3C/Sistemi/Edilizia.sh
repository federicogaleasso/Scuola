#Galeasso Federico
#Compito
#Una ditta di costruzioni compra il seguente materiale:
#X sacchi di cemento a 5€ al sacco (X chiesto in input all'utente)
#30 sacchi di ghiaia al prezzo complessivo di... (da chiedere all'utente)
#Y carriole a 50€ l'una (Y chiesto in input)
#20 caschi di sicurezza al prezzo complessivo di... (da chiedere all'utente)
#15 bidoni di vernice al prezzo complessivo di... (da chiedere all'utente)
#Calcolare il totale fattura che dovrà pagare la ditta sapendo che al totale si dovrà aggiungere il 22% di IVA e il fisso di 50€ per la #consegna del materiale.
#Se il totale finale (comprensivo di IVA e di consegna) sarà maggiore di 1000 euro, verrà applicato uno sconto del 5%.
#Visualizzare in output la spesa finale complessiva.
PrezzoX=5
NumSG=30
PrezzoY=50
NumCS=20
NumBV=15
IVA=22
PrezzoConsegna=50
Sconto=-5
Num=1000
echo -n "Inserisci i sacchi di cemento: "
read X
echo -n "Inserisci il prezzo dei sacchi di ghiaia: "
read PrezzoSG
echo -n "Inserisci il numero di carriole: "
read Y
echo -n "Inersici il prezzo dei caschi di sicurezza: "
read PrezzoCS
echo -n "Inserisci il prezzo dei bidoni di vernice: "
read PrezzoBV
XTOT=$(( X*PrezzoX ))
SGTOT=$(( PrezzoSG*NumSG ))
YTOT=$(( Y*PrezzoY ))
CSTOT=$(( PrezzoCS*NumCS ))
BVTOT=$(( PrezzoBV*NumBV ))
Fattura=$(( (XTOT+SGTOT+YTOT+CSTOT+BVTOT+PrezzoConsegna)*IVA/100 ))
echo "$Fattura"
if [[ $Fattura -gt $Num ]]
then
ScontoFattura=$(( (Fattura*Sconto)/100 ))
echo "$ScontoFattura"
fi
