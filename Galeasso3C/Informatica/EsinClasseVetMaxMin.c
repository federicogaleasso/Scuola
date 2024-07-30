/*
Galeasso Federico 3C 22/2/2022 Esercizio in classe VETTORI MAX e MIN

Caricare un vettore con N numeri (N scelto dall'utente e compreso tra 4 e 50) interi casuali compresi tra 27 e 112.
Ricavare il massimo ed il minimo del vettore e la posizione della loro prima occorrenza.
Calcolare e stampare inoltre il numero di occorrenze per il valore massimo e per il valore minimo.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
int creaRandom(int, int);

int main(){
	int vet[51], N=0, i=0, contatoreMax=0, contatoreMin=113, posizioneMin=0, posizioneMax=0, occorrenzeMax=0, occorrenzeMin=0;
	srand(time(NULL));
	printf("Inserisci la quantità di numeri tra 4 e 50 --> ");
	scanf("%d", &N);
	while(N<4 || N>50){
		printf("Inserisci la quantità di numeri tra 4 e 50 --> ");
		scanf("%d", &N);
	}
	for(i=0; i<N; i++){
		vet[i]=creaRandom(112, 27);
		printf("%d | ", vet[i]);
		if(vet[i]>contatoreMax){
			contatoreMax=vet[i];
			posizioneMax=i;
		}
		if(vet[i]<contatoreMin){
			contatoreMin=vet[i];
			posizioneMin=i;
		}
		if(contatoreMax == vet[i]){
			contatoreMax++;
		}
		if(contatoreMin == vet[i]){
			contatoreMin++;
		}
	}
	printf("\n");
	printf("Il numero massimo è %d\n", contatoreMax);
	printf("La posizione del numero massimo è %d\n", posizioneMax);
	printf("Il numero di occorrenze del numero massimo è %d\n", occorrenzeMax);	
	printf("Il numero minimo è %d\n", contatoreMin);
	printf("La posizione del numero minimo è %d\n", posizioneMin);
	printf("Il numero di occorrenze del numero minimo è %d\n", occorrenzeMin);	
return 0;
}

int creaRandom(int max, int min){
	return rand()%(max-min+1)+min;
}
