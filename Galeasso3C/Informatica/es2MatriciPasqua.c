/*
Galeasso Federico 3C 16/4/2022 Es 2 Matrici Pasqua

es.2 - Ricerca di elementi
- Chiedere all'utente il num di righe e il num di colonne della matrice (massimo 10 x entrambi altrimenti richiederli nuovamente).

- Riempire la matrice di valori random da 8 a 64

- Dato un valore immesso dall'utente (tra 8 e 64), ricercare se esso esiste (almeno una volta) nella matrice. In caso affermativo, stampare la riga e la colonna del dato trovato.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
int creaRandom(int, int);
void caricaMatrice(int, int, int[][MAX]);
void stampaMatrice(int, int, int[][MAX]);
void cercaNumero(int, int, int[][MAX]);

int main(){
	int matrice[MAX][MAX], r=11, c=-1, i=0, j=0;
	char invio=' ';
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
	cercaNumero(r, c, matrice);

return 0;
}

void caricaMatrice(int r, int c, int matrice[][MAX]){
	int i, j;
	
	for(i=0; i<r; i++){
		for(j=0; j<c; j++){
			matrice[i][j]=creaRandom(8,64);
		}
	}

}

void stampaMatrice(int r, int c, int matrice[][MAX]){
	int i, j;

	for(i=0; i<r; i++){
		for(j=0; j<c; j++){	
			printf("\e[1;34m%d\t\e[0;37m", matrice[i][j]);
		}
		printf("\n");
	}

}

int creaRandom(int min, int max){
return rand()%(max-min+1)+min;
}

void cercaNumero(int r, int c, int matrice[][MAX]){
	int i, j, numero=0, riga=0, colonna=0, flag=0;
	
	printf("\e[1;33mInserisci un \e[1;34mnumero\e[0;37m \e[1;33me verrà ricercato nella matrice (tra 8 e 64): \e[0;37m");
	scanf("%d", &numero);
	while(numero<8 || numero>64){
		printf("\e[1;31mERRORE!\e[0;37m \e[1;33mInserisci un \e[1;34mnumero\e[0;37m \e[1;33me verrà ricercato nella matrice (tra 8 e 64): \e[0;37m");
		scanf("%d", &numero);
	}
	printf("\n");
	for(i=0; i<r; i++){
		for(j=0; j<c; j++){	
			if(matrice[i][j]==numero){
				riga=i;
				colonna=j;
				printf("\e[1;32mNUMERO TROVATO!\e[0;37m \e[1;33mIl numero \e[1;34m%d\e[0;37m \e[1;33mè presente nella riga \e[1;32m%d\e[0;37m \e[1;33me nella colonna \e[1;32m%d\e[0;37m\e[0;37m\n\n", numero, riga, colonna);
				flag=1;
			}
		}
	}
	if(flag==0){
		printf("\e[1;31mNUMERO NON TROVATO!\e[0;37m \e[1;33mIl numero \e[1;34m%d\e[0;37m \e[1;33mnon è presente nella matrice\e[0;37m\n\n", numero);
	}
}
