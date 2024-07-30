/*
Galeasso Federico 3C
Dati due numeri, calcolare la somma e stampare a video.
*/

#include <stdio.h>
int main (){
	//Dichiarazione variabili
	int N1, N2, SOMMA;
	printf("Inserisci il primo numero: \n");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: \n");
	scanf("%d", &N2);
	SOMMA=N1+N2;
	printf("La somma di %d+%d vale %d\n", N1, N2, SOMMA);
return 0;
}
