/*
GALEASSO FEDERICO 3C COMPITI ESTIVI

Realizzare un programma che permetta di salvare le statistiche di diverse squadre di calcio (N
squadre, con N compreso tra 3 e 5).
Per ogni squadra, il programma, deve permettere di specificare il nome, salvato in un apposito array
di stringhe.

Il programma deve memorizzare (in apposite strutture) ed in seguito visualizzare per ogni squadra, i
dati personali di tutti i giocatori (X giocatori con X compreso tra 2 e 6):
a) il cognome del giocatore;
b) la squadra di appartenenza;
c) il numero di maglia;
d) il numero di goal segnati (subiti, se è un portiere).

Dopo aver acquisito i dati necessari, calcolare:
1. il totale dei goal segnati da ogni squadra, specificando:
◦ i goal segnati dagli attaccanti (numero di maglia da 7 a 11);
◦ i goal segnati dai centrocampisti (numero di maglia da 4 a 6);
◦ i goal segnati dai difensori (numero di maglia da 1 a 3);
2. il totale dei goal subiti dalla squadra.
3. il nome della squadra che ha subito meno reti
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX 250
#define A 100
#define R 5
#define C 101

int main() {

	//dichiarazione variabili
	int i, j, N, ngioc, z, tmpP, tmpI, portieri[R], attaccanti[R], centrocampisti[R], difensori[R], nmaglia[A], reti[A];
	char giocatori[A][C], squadre[R][C], tmp[MAX];

	//richiesta numero di squadre
	printf("Numero di SQUADRE (tra 3 e 5): ");
	scanf("%d", &N);

	//controllo numero di squadre
	while (N < 3 || N > 5) {
		printf("ERRORE!!! Numero di SQUADRE (tra 3 e 5): ");
		scanf("%d", &N);
	}

	for (i = 0; i < N; i++) {
		while (getchar() == "\n");
		
		//richiesta nome della squadra
		printf("NOME %d° squadra: ", i + 1);
		gets(tmp);
		strcpy(squadre[i], tmp);
		
		//richiesta numero dei giocatori
		printf("Numero GIOCATORI (tra 3 e 6): ");
		scanf("%d", &ngioc);
		
		//controllo numero dei giocatori
		while (ngioc < 2 || ngioc > 6) {
			printf("ERRORE!!! Numero GIOCATORI (tra 3 e 6): ");
			scanf("%d", &ngioc);
		}
		
		//richiesta cognome giocatore
		for (j = 0; j < ngioc; j++) {
			while (getchar() == "\n");
			printf("COGNOME giocatore %d: ", j + 1);
			gets(tmp);
			
			switch (i) {
				case 0:
					z = j;
					break;
				case 1:
					z = j + 5;
					break;
				case 2:
					z = j + 11;
					break;
				case 3:
					z = j + 17;
					break;
				case 4:
					z = j + 23;
					break;
			}
			
			strcpy(giocatori[z], tmp);
			
			//richiesta numero di maglia
			printf("NUMERO MAGLIA giocatore %d: ", j + 1);
			scanf("%d", &nmaglia[z]);
			
			//richiesta goal fatti/subiti
			printf("GOL (fatti/subiti):  ");
			scanf("%d", &reti[z]);		
			
			//goal segnati dagli attaccanti
			if (nmaglia[z] >= 7 && nmaglia[z] <= 11) {
				attaccanti[i] = attaccanti[i] + reti[z];
			}
			
			//goal segnati dai centrocampisti
			if (nmaglia[z] >= 4 && nmaglia[z] <= 6) {
				centrocampisti[i] = centrocampisti[i] + reti[z];
			}
			
			//goal segnati dai difensori
			if (nmaglia[z] >= 1 && nmaglia[z] <= 3) {
				difensori[i] = difensori[i] + reti[z];
			}
			
			//goal subiti dai portieri
			if (nmaglia[z] < 1 || nmaglia[z] > 11) {
				portieri[i] = portieri[i] + reti[z];
			}
		}
	}

	//stampa resoconti
	for (i = 0; i < N; i++) {
		printf("\n");
		printf("SQUADRA: %s \n", squadre[i]);	
		for (j = 0; j < ngioc; j++) {
			printf("GIOCATORE: %s \n", giocatori[j]);
			printf("MAGLIA: %d \n", nmaglia[j]);
			printf("GOAL: %d \n", reti[j]);
		}
	}

	//stampa dei goal totali e dei goal tra attaccanti-centrocampisti-difensori + goal subiti dalla squadra
	for (i = 0; i < N; i++) {
		printf("\n");
		printf("Goal TOTALI squadra %d: %d \n", i + 1, attaccanti[i] + centrocampisti[i] + difensori[i]);
		printf("Goal SUBITI squadra %d: %d \n", i + 1, portieri[i]);
		printf("ATTACANTI: %d \n",attaccanti[i]);
		printf("CENTROCAMPISTI: %d \n", centrocampisti[i]);
		printf("DIFENSORI: %d \n", difensori[i]);
	}

	tmpP = portieri[0];
	tmpI = 0;
	for (i = 0; i < N; i++) {
		if (tmpP > portieri[i]) {
			tmpP = portieri[i];
			tmpI = i;
		}
	}
	printf("\n");
	
	//stampa della squadra che ha subito meno reti
	printf("La squadra %s è quella che ha subito meno reti.\n", squadre[tmpI]);

return 0;
}
