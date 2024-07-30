/*
Numero Maggiore
Dati due numeri, stabilire il maggiore
Galeasso Federico 3C 12/10/2021
*/
#include <stdio.h>
int main(){
	int N1, N2;
	printf("\n*****Calcolo del numero maggiore*****\n");
	printf("\nInserisci il primo numero: \n");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: \n");
	scanf("%d", &N2);
	printf("\n----------------------------\n");
	if (N1>N2){
	printf("\nIl numero maggiore è %d\n\n", N1);
	}
	else{
	printf("\nIl numero maggiore è %d\n\n", N2);
	}
return 0;
}
