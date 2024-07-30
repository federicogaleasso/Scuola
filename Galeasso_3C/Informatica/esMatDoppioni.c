/*
Galeasso Federico 3C 1/5/2022 Esercizio MATRICI contorno

Avendo una matrice di caratteri NxM con N e M richiesti in input all'utente e compresi tra 7 e 23, riempirla di caratteri alfabetici casuali minuscoli o maiuscoli (A-Z e a-z ...trovare un sistema per rendere casuale anche la possibilità che sia maiuscolo o minuscolo).
Stampare la matrice riempita.
Cercare per ogni elemento della matrice se c'è un suo doppione nella cornice di caratteri che lo "contorna" e in tal caso sostituire questi caratteri della cornice con soli '0' (zero).
Ristampare la matrice risultante.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 23

//PROTOTIPI
int creaRandomMaiuscole(char, char);
int creaRandomMinuscole(char, char);
int creaRandom(int, int);
void caricaMatrice(int, int, char[][MAX]);
void stampaMatrice(int, int, char[][MAX]);
void cercaDoppioni(int, int, char[][MAX]);

int main(){
	int r=24, c=6, i=0, j=0;
	char invio=' ', matrice[MAX][MAX];
	srand(time(NULL));
	system("clear");
	printf("\e[1;35m*** BENVENUTO ***\e[0;37m\n\n");
	printf("\e[1;36mPremi invio per cominciare...\e[0;37m");
	scanf("%c", &invio);
	printf("\n");
	while(r>MAX || r<7){
		printf("\e[1;33mInserisci il numero di \e[0;37m\e[1;32mrighe\e[0;37m\e[1;33m:\e[0;37m ");
		scanf("%d", &r);
	}
	
	while(c>MAX || c<7){
		printf("\e[1;33mInserisci il numero di \e[0;37m\e[1;32mcolonne\e[0;37m\e[1;33m:\e[0;37m ");
		scanf("%d", &c);
	}
	
	caricaMatrice(r, c, matrice);
	printf("\n");
	printf("\e[1;33m-- Stampo la \e[1;34mmatrice\e[0;37m \e[1;33m--\e[0;37m\n\n");
	stampaMatrice(r, c, matrice);
	printf("\n");
	cercaDoppioni(r, c, matrice);
	printf("\n");
	stampaMatrice(r, c, matrice);
return 0;
}

void caricaMatrice(int r, int c, char matrice[][MAX]){
	int i, j, number=0;
	
	number=creaRandom(0, 1);
	for(i=0; i<r; i++){
		for(j=0; j<c; j++){
			if(number==0){
				matrice[i][j]=creaRandomMaiuscole('A','Z');
			}
			if(number==1){
				matrice[i][j]=creaRandomMinuscole('a','z');
			}
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

void cercaDoppioni(int r, int c, char matrice[][MAX]){
	int i, j, k=0, z, y;
	
	for(i=1; i<r-1; i++){
        for(j=1; j<c-1; j++){
            for(y=i-1; y<i+1;y++){
                for(z=j-1; z<j+1;z++){
                    if(i!=y && j!=z){
                        if(matrice[i][j]==matrice[y][z] && matrice[y][z]!='0'){
                            k=1;
                        }
                    }        
                }
            }
            for(y=i-1; y<i+1;y++){
                for(z=j-1; z<j+1;z++){
                    if(i!=y && j!=z){
                        matrice[y][z]='0';
                    }
                }
            }
        }
    }
}

int creaRandomMaiuscole(char A, char Z){
return rand()%('Z'-'A'+1)+'A';
}

int creaRandomMinuscole(char a, char z){
return rand()%('z'-'a'+1)+'a';
}

int creaRandom(int min, int max){
return rand()%(max-min+1)+min;
}
