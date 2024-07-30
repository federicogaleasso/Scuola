/*
Galeasso Federico 3C 16/4/2022 Es 1 Matrici Pasqua

es.1 sulle matrici:

- Chiedere all'utente il valore del lato l della matrice quadrata (massimo 10 altrimenti richiedere nuovamente l)

- Riempire con numeri casuali tra 10-25 inclusi ogni cella della matrice di lato l.

- Calcolare la somma di ogni riga e stamparla.

- Calcolare la somma di ogni colonna e stamparla.

- Stampare il valore medio della matrice.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
int creaRandom(int, int);
void caricaMatrice(int, int[][MAX]);
void stampaMatrice(int, int[][MAX]);
void calcolaMatrice(int, int[][MAX]);

int main(){
	int matrice[MAX][MAX], l=11, i=0, j=0;
	char invio=' ';
	srand(time(NULL));
	system("clear");
	printf("\e[1;35m*** BENVENUTO ***\e[0;37m\n\n");
	printf("\e[1;36mPremi invio per cominciare...\e[0;37m");
	scanf("%c", &invio);
	printf("\n");
	
	while(l>MAX || l<0){
		printf("\e[1;33mInserisci il valore di un \e[0;37m\e[1;32mlato\e[0;37m \e[1;33mdella \e[1;34mmatrice quadrata\e[0;37m\e[1;33m (massimo 10!):\e[0;37m ");
		scanf("%d", &l);
	}
	
	caricaMatrice(l, matrice);
	printf("\n");
	printf("\e[1;33m-- Stampo la \e[1;34mmatrice\e[0;37m \e[1;33m--\e[0;37m\n\n");
	stampaMatrice(l, matrice);
	printf("\n");
	calcolaMatrice(l, matrice);
	printf("\n");
	
return 0;
}

int creaRandom(int min, int max){
return rand()%(max-min+1)+min;
}

void caricaMatrice(int l, int matrice[][MAX]){
	int i, j;
	for(i=0; i<l; i++){
		for(j=0; j<l; j++){
			matrice[i][j]=creaRandom(10, 25);
		}
	}

}

void stampaMatrice(int l, int matrice[][MAX]){
	int i, j;
	for(i=0; i<l; i++){
		for(j=0; j<l; j++){
			printf("\e[1;34m%d\t\e[0;37m", matrice[i][j]);
		}
		printf("\n");
	}

}

void calcolaMatrice(int l, int matrice[][MAX]){
	int i, j, somma=0;
	float media=0.0;
	
	for(i=0; i<l; i++){
		for(j=0; j<l; j++){
			somma=somma+matrice[i][j];
		}
	}
	printf("\e[1;33mLa \e[0;37m\e[1;32msomma\e[0;37m\e[1;33m vale:\e[0;37m \e[1;34m%d\e[0;37m\n", somma);
	
	for(i=0; i<l; i++){
		for(j=0; j<l; j++){
			media=(float)somma/l;
		}
	}
	printf("\e[1;33mLa \e[0;37m\e[1;32mmedia\e[0;37m\e[1;33m vale:\e[0;37m \e[1;34m%.2f\e[0;37m\n", media);
}
