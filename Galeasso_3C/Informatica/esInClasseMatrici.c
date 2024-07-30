/*
Galeasso Federico 3C 26/4/2022 Esercizio in classe MATRICI

Avendo una matrice di caratteri NxM con N e M richiesti in input all'utente e compresi tra 2 e 10, riempirla di caratteri alfabetici MAIUSCOLI casuali (A-Z).
Contare e stampare per ogni riga il numero di vocali e restituire la riga che ha il numero di vocali maggiori.
Contare e stampare, sulla cornice di contorno della matrice, le occorrenze del carattere 'F'.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
int creaRandom(char, char);
void caricaMatrice(int, int, char[][MAX]);
void stampaMatrice(int, int, char[][MAX]);
void cercaVocali(int, int, char[][MAX]);

int main(){
	int r=11, c=-1, i=0, j=0;
	char invio=' ', matrice[MAX][MAX];
	srand(time(NULL));
	system("clear");
	printf("\e[1;35m*** BENVENUTO ***\e[0;37m\n\n");
	printf("\e[1;36mPremi invio per cominciare...\e[0;37m");
	scanf("%c", &invio);
	printf("\n");
	while(r>MAX || r<0){
		printf("\e[1;33mInserisci il numero di \e[0;37m\e[1;32mrighe\e[0;37m\e[1;33m:\e[0;37m ");
		scanf("%d", &r);
	}
	
	while(c>MAX || c<0){
		printf("\e[1;33mInserisci il numero di \e[0;37m\e[1;32mcolonne\e[0;37m\e[1;33m:\e[0;37m ");
		scanf("%d", &c);
	}
	
	caricaMatrice(r, c, matrice);
	printf("\n");
	printf("\e[1;33m-- Stampo la \e[1;34mmatrice\e[0;37m \e[1;33m--\e[0;37m\n\n");
	stampaMatrice(r, c, matrice);
	printf("\n");
	cercaVocali(r, c, matrice);
return 0;
}

void caricaMatrice(int r, int c, char matrice[][MAX]){
	int i, j;
	
	for(i=0; i<r; i++){
		for(j=0; j<c; j++){
			matrice[i][j]=creaRandom('A','Z');
		}
	}
}

void stampaMatrice(int r, int c, char matrice[][MAX]){
	int i, j;

	for(i=0; i<r; i++){
		for(j=0; j<c; j++){	
			printf("\e[1;34m%c\t\e[0;37m", matrice[i][j]);
		}
		printf("\n");
	}

}

int creaRandom(char A, char Z){
return rand()%('Z'-'A'+1)+'A';
}

void cercaVocali(int r, int c, char matrice[][MAX]){
	int i, j, cont=0, maxVCol=0;
	
	for(i=0; i<r; i++){
		cont=0;
		for(j=0; j<c; j++){	
			if(matrice[i][j] == 'A' || matrice[i][j] == 'E' || matrice[i][j] == 'I' || matrice[i][j] == 'O' || matrice[i][j] == 'U'){
				cont=cont+1;
			}
			 if(cont > maxVCol){
            maxVCol=cont;
            maxVCol=i;
        }
		}
		printf("\e[1;33mIl totale delle vocali della \e[1;34m%d° \e[0;37m\e\e[1;32mriga\e[0;37m\e[1;33m è: \e[1;34m%d\e[0;37m\e\e[0;37m", (i+1), cont);
		printf("\n");
	}
	printf("\n\e[1;33mLa \e[1;34m%d° \e[0;37m\e\e[1;32mriga\e[0;37m\e[1;33m è quella con il numero maggiore di vocali\n\n", (i+1));
}
