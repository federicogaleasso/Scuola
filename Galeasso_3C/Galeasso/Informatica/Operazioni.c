/*
Galeasso Federico 3C
Scrivere un programma che richieda due numeri interi in input (N1 e N2) e svolga le operazioni date.
*/

#include <stdio.h>
#include <math.h>
int main (){
	int N1=0, N2=0, Somma=0, Sottrazione=0, Moltiplicazione=0, DivisioneQI=0, Restodivisione=0, CambiosegnoN1=0, CambiosegnoN2=0, Elevpotenza=0;
	float DivisioneQR=0;
	printf("\n*****CALCOLATRICE*****\n\n");
	printf("Inserisci il primo numero: \n");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: \n");
	scanf("%d", &N2);
	printf("\n****************************\n");
	Somma=N1+N2;
	Sottrazione=N1-N2;
	Moltiplicazione=N1*N2;
	DivisioneQI=N1/N2;
	Restodivisione=N1%N2;
	DivisioneQR=(float)N1/N2;
	CambiosegnoN1=-N1;
	CambiosegnoN2=-N2;
	Elevpotenza=pow (N1, N2);
	printf("\nIl risultato di %d+%d vale %d\n", N1, N2, Somma);
	printf("Il risultato di %d-%d vale %d\n", N1, N2, Sottrazione);
	printf("Il risultato di %d*%d vale %d\n", N1, N2, Moltiplicazione);
	printf("Il risultato di %d/%d vale %d\n", N1, N2, DivisioneQI);
	printf("Il resto di %d/%d è %d\n", N1, N2, Restodivisione);
	printf("Il risultato di %d/%d vale %f\n", N1, N2, DivisioneQR);
	printf("Cambio di segno del numero %d: %d\n", N1, CambiosegnoN1);
	printf("Cambio di segno del numero %d: %d\n", N2, CambiosegnoN2);
	printf("L'elevamento a potenza %d^%d vale %d\n\n", N1, N2, Elevpotenza);
return 0;
}
