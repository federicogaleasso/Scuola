//Galeasso Federico 3C 9/3/2022 BUBBLE SORT

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
void bubbleSort(int, int[]);
void riempiVett(int, int[]);
int creaRandom(int, int);
void stampaVett(int, int[]);

int main(){
	int vett[20], N, invio;
	srand(time(NULL));
	printf("Inserisci la lunghezza del vettore (tra 1 e 20 elementi) --> ");
	scanf("%d", &N);
	while(N<=0 || N>20){
		printf("ERRORE! Reinserisci la lunghezza del vettore (tra 1 e 20 elementi) --> ");
		scanf("%d", &N);
	}
	riempiVett(N, vett);
	stampaVett(N, vett);
	printf("Procedo ora con l'ordinamento del vettore...");
	printf("Premi invio per continuare...\n");
	scanf("%d", &invio);
	bubbleSort(N, vett);
	printf("Stampo il vettore ordinato...");
return 0;
}

void bubbleSort(int N, int V[]){
	int I, J, FLAG, TMP;
	J=N;
	FLAG=1; //true --> 1 | false --> 0
	while(FLAG == 1){
		FLAG=0;
		for(I=0; I<J-1; I++){
			if(V[I] > V[I+1]){
				TMP=V[I];
				V[I]=V[I+1];
				V[I+1]=TMP;
				FLAG=1;
			}
		}
	}
	J=J-1;
}

void riempiVett(int lung, int vetnum[]){
	int i;
	for(i=0; i<lung; i++){
		vetnum[i]=creaRandom(1,100);
	}
}

void stampaVett(int lung, int vetnum[]){
	int i;
	for(i=0; i<lung; i++){
		printf("|%d\t|\n", vetnum[i]);
	}
}

int creaRandom(int min, int max){
return rand()%(max-min+1)+min;
}
