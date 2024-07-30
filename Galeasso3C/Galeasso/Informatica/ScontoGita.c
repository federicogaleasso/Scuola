/*
Compito
Dato il prezzo della quota di una gita ed il numero di persone partecipanti, calcolare l’importo totale.
Se l’importo supera i 500 €, viene effettuato uno sconto del 10% sull’importo totale.
Se l’importo è compreso tra 300€ e 500€ inclusi, lo sconto è invece del 7% sull’importo totale.
Altrimenti, lo sconto è del 2%.
Visualizzare: l’importo finale, l’importo per persona e lo sconto effettuato nella forma: “Ho fatto uno sconto del [xy%] e quindi ho scalato [zx€] dal totale”.
Galeasso Federico 3C 16/10/2021
*/
#include <stdio.h>
int main(){
	int NPersone, Sconto1=10, Sconto2=7, Sconto3=2, Soldi1=500, Soldi2=300;
	float PrezzoGita, ImpTOT, Piùdi500, Tra300e500, Altrimenti;
	printf("Inserisci il prezzo della quota della gita: ");
	scanf("%f", &PrezzoGita);
	printf("Inserisci il numero di persone partecipanti: ");
	scanf("%d", &NPersone);
	ImpTOT=PrezzoGita*NPersone;
	if(ImpTOT>Soldi1){
		Piùdi500=(float)(ImpTOT*Sconto1)/100;
		printf("L'importo totale è di %f\n", Piùdi500);
	}
	else{
		if(ImpTOT>=Soldi2){
			Tra300e500=(float)(ImpTOT*Sconto2)/100;
			printf("L'importo totale è di %f\n", Tra300e500);
		}
		else{
			Altrimenti=(float)(ImpTOT*Sconto3)/100;
			printf("Limporto totale è di %f\n", Altrimenti);
		}
	}
return 0;
}
