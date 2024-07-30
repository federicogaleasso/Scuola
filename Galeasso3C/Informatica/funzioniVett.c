/*
Galeasso Federico 3C 22/2/2022 Esercizio in classe passaggio PARAMETRI di tipo VETTORE con le FUNZIONI
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
int dimVet(int, int);
void caricaVet(int, int[]);		//passaggio VETTORE per parametro, punta nel primo indirizzo di cella del vettore
void stampaVet(int, int[]);

int main(){
	int dimensione=0, numeri[30];
	srand(time(NULL));
	dimensione=dimVet(4,25);
	caricaVet(dimensione, numeri);
	stampaVet(dimensione, numeri);
return 0;
}

int dimVet(int minimo, int massimo){
	int dim;
	printf("Dimensione vettore --> ");
	scanf("%d", &dim);
	while(dim<minimo || dim>massimo){
		printf("Errore! Inserisci nuovamente la dimensione vettore --> ");
		scanf("%d", &dim);
	}
return dim;
}

void caricaVet(int dimv, int vet[]){
	int i=0, numeri[30];
	for(i=0; i<dimv; i++){
		vet[i]=rand()%11;
	}
}

void stampaVet(int dimve, int vett[]){
	int i=0;
	for(i=0; i<dimve; i++){
		printf("%d | ", vett[i]);
	}
	printf("\n");
}
