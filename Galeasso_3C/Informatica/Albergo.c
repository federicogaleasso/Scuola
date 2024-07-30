/*Galeasso Federico
Codifica algoritmo verfica 26/10/2021
*/
#include <stdio.h>
int main (){
	int Ngiorni=0, Camera=0, Trattamento=0;
	float PrezzoCamera=0, PercTrattamento=0, Totale=0, SpeseSoggiorno=0, TariffaSoggiorno=2.5;
	printf("Benvenuti nell'hotel Sogni d'Oro\n");
	while (Ngiorni<1){
		printf("Quanti giorni vuoi prenotare? ");
		scanf("%d", &Ngiorni);
	}
	printf("Che tipo di camera vuoi prenotare? 1 per Singola, 2 per Doppia: ");
	scanf("%d", &Camera);
	if(Camera==1){
		PrezzoCamera=40;
		printf("Il prezzo della camera è %.2f€\n", PrezzoCamera);
	}
	else{
		PrezzoCamera=75;
		printf("Il prezzo della camera è %.2f€\n", PrezzoCamera);
	}
		Totale=Ngiorni*PrezzoCamera;
		printf("Che tipo di trattamento vuoi prenotare? 1 per Pensione completa, 2 per Mezza pensione, 3 per B&B: ");
		scanf("%d", &Trattamento);
		if(Trattamento==1){
			PercTrattamento=0.3;
			printf("Il trattamento è di %.2f€\n", PercTrattamento);
		}
		else{
			if(Trattamento==2){
				PercTrattamento=0.15;
				printf("Il trattamento è di %.2f€\n", PercTrattamento);
			}
			else{
				printf("Nessuna maggioranza\n");
			}
		}
		Totale=Totale+(Totale*PercTrattamento);
		SpeseSoggiorno=Ngiorni*TariffaSoggiorno;
		Totale=Totale+SpeseSoggiorno;
		printf("Il totale speso per il soggiorno è %.2f€\n", Totale);
return 0;
}
