/*
Esesrcizio
Sul prezzo di un prodotto viene praticato lo sconto dell’X% se si acquistano fino a 10 pezzi e dell’Y% se si acquistano più di 10 pezzi. Presi in input il prezzo di un prodotto e il numero di pezzi da acquistare, visualizza la spesa da sostenere.
Galeasso Federico 3C 14/10/2021
*/
#include <stdio.h>
int main (){
	int NPezzi, Sconto1=5, Sconto2=10;
	float Prezzo, SpesaTOT1, SpesaTOT2;
	printf("Inserisci il prezzo del prodotto: ");
	scanf("%f", &Prezzo);
	printf("Inserisci il numero di pezzi: ");
	scanf("%d", &NPezzi);
	if (NPezzi==10){
		SpesaTOT1=((Prezzo*NPezzi)*Sconto1)/100;
		printf("La spesa totale è %.2f\n", SpesaTOT1);
	}
		else{
			if(NPezzi>0){
				SpesaTOT1=((Prezzo*NPezzi)*Sconto1)/100;
				printf("La spesa totale è %.2f\n", SpesaTOT2);
			}
		}
return 0;
}
