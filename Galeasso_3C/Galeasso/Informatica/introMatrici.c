//Galeasso Federico 3C 12/4/2022 Introduzione Matrici

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
void caricaMatrice(int, int, int[][MAX]);
void stampaMatrice(int, int, int[][MAX]);

int main(){
	int numeri[MAX][MAX], r=11, c=-1, i=0, j=0;
	srand(time(NULL));
	
	//Controllo su RIGHE
	while(r>MAX || r<0){
		printf("Quante righe? ");
		scanf("%d", &r);
	}
	
	//Controllo su COLONNE
	while(c>MAX || c<0){
		printf("Quante colonne? ");
		scanf("%d", &c);
	}
	
	caricaMatrice(r, c, numeri);
	stampaMatrice(r, c, numeri);
	
	/*
	
	//Riempimento MATRICE
	for(i=0; i<r; i++){		//Cicla per le RIGHE
		for(j=0; j<c; j++){	//Cicla per le COLONNE
			numeri[i][j]=rand()%11;
		}
	}
	
	//Stampa MATRICE
	for(i=0; i<r; i++){		//Cicla per le RIGHE
		for(j=0; j<c; j++){	//Cicla per le COLONNE
			printf("%d\t", numeri[i][j]);
		}
		printf("\n");
	}
	
	*/
return 0;
}

void caricaMatrice(int r, int c, int numeri[][MAX]){
	int i, j;
	
	//Riempimento MATRICE
	for(i=0; i<r; i++){		//Cicla per le RIGHE
		for(j=0; j<c; j++){	//Cicla per le COLONNE
			numeri[i][j]=rand()%11;
		}
	}

}

void stampaMatrice(int r, int c, int numeri[][MAX]){
	int i, j;
	
	//Stampa MATRICE
	for(i=0; i<r; i++){		//Cicla per le RIGHE
		for(j=0; j<c; j++){	//Cicla per le COLONNE
			printf("%d\t", numeri[i][j]);
		}
		printf("\n");
	}

}
