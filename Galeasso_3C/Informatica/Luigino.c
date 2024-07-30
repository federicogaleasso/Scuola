/*
Il piccolo Luigino va al bar e compra delle caramelle che costano 0,50€ l'una, delle barrette di cioccolata che costano 2,50€ l'una e dei gelati che costano 3€ l'uno (chiedere in input il numero di caramelle, barrette e gelati).
Calcolare e comunicare l'importo totale.

Se l'importo totale è uguale a zero, segnalare "Luigino! Non hai comprato niente, ritorna dentro!", altrimenti chiedi a Luigino quanti soldi ha in tasca e:

- se l'importo totale è maggiore dire "Luigino, hai comprato troppa roba, non hai abbastanza soldi"
- altrimenti calcolare il resto che dovrebbe ricevere Luigino e visualizzarlo in output

Galeasso Federico 3C 12/10/2021
*/
#include <stdio.h>
int main (){
	int Gelati, Caramelle, Barrette;
	float CostoCaramelle=0.50, CostoBarrette=2.50, CostoGelati=3, CostoTOT, Solditasca, Resto;
	printf("Inserisci il numero di caramelle:\n");
	scanf("%d", &Caramelle);
	printf("Inserisci il numero di barrette:\n");
	scanf("%d", &Barrette);
	printf("Inserisci il numero di gelati:\n");
	scanf("%d", &Gelati);
	CostoTOT=(float)(CostoCaramelle*Caramelle)+(CostoBarrette*Barrette)+(CostoGelati*Gelati);
	printf("Il costo totale è di %.2f\n", CostoTOT);
	if(CostoTOT==0){
		printf("Luigino! Non hai comprato niente, ritorna dentro!\n");
	}
		else{
			printf("Luigino, quanti soldi hai in tasca?\n");
			scanf("%f", &Solditasca);
		}
				if(CostoTOT>Solditasca){
					printf("Luigino, hai comprato troppa roba, non hai abbastanza soldi!\n");	
				}
					else{
						Resto=(float)Solditasca-CostoTOT;
						printf("Il resto di Luigino è di %.2f\n", Resto);
					}
return 0;
}
