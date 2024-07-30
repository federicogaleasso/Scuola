/*
Numero Uguale o Maggiore
Dati due numeri, stabilire se sono uguali. Se sono diversi, stablire il magggiore.
Galeasso federico 3C 12/10/2021
*/
#include <stdio.h>
int main(){
	int N1, N2;
	printf("\nInserisci il primo numero: \n");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: \n");
	scanf("%d", &N2);
	if (N1==N2){
	printf("\nI due numeri sono uguali\n\n");
	}
	else{
		if (N1>N2){
			printf("\nIl numero maggiore è %d\n\n", N1);
		}
		else{
			printf("\nIl numero maggiore è %d\n\n", N2);
		}
	}
return 0;
}
