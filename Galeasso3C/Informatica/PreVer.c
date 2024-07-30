/*
Galeasso Federico 3C
Scrivere un programma in linguaggio C che legga da tastiera una sequenza di lunghezza ignota a priori di numeri interi positivi. Il programma, a partire dal primo numero introdotto, stampa ogni volta la media di tutti i numeri introdotti. Terminare quando il numero inserito è negativo.
*/
#include <stdio.h>
int main (){
	int N=1, Numero=1;
	float MediaTOT, TOTALE=0;
		while(N>=0){
			printf("Inserisci il %d° numero: ", Numero);
			scanf("%d", &N);
			TOTALE=TOTALE+N;
			MediaTOT=TOTALE/Numero;
			Numero=Numero+1;
			printf("La media dei numeri inseriti è %.2f\n", MediaTOT);
		}
return 0;
}
