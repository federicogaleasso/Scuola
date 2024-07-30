/*
Galeasso federico 3C 30/11/2021 Esercizio Cesare

Scrivere un programma che ricrei il cifrario di Cesare.
Il programma dovrà accettare una parola di 4 caratteri minuscoli, convertirli in maiuscolo, chiedere la chiave di codifica e stampare il testo cifrato.
La chiave di codifica serve per "traslare" le lettere sull'alfabeto.

Es.
CASA chiave di codifica 3 diventa FDVD
*/
#include <stdio.h>
int main(){
	int i, COD;
	char c;
	printf("Codifica --> ");
	scanf("%d", &COD);
	printf("Inserisci una parola di 4 caratteri: ");
	for(i=0; i<5; i++){
		scanf("%c", &c);
		c=c+COD;
		printf("%c", c-32);
	}
	printf("\n");
return 0;
}
