/*
Galeasso Federico 3C 15/11/2021
Scrivere un programma che visualizzi un rettangolo la cui cornice sia costituita da caratteri asterisco, la parte interna da caratteri Q e dove il numero di righe del rettangolo sia deciso dall'utente e il numero di colonne invece estratto con un random (ciascuno di questi numeri non deve essere inferiore a 3).

Per esempio, se il numero delle righe è uguale a 5 e il numero di
colonne a 21, sul video deve apparire:

*********************
*QQQQQQQQQQQQQQQQQQQ*
*QQQQQQQQQQQQQQQQQQQ*
*QQQQQQQQQQQQQQQQQQQ*
*********************
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL));
	
	int Righe=0, Colonne=0, i, j;
	
	printf("Inserisci il numero di righe: ");
	scanf("%d", &Righe);
	while(Righe<3){
		printf("Hai inserito un numero minore di 3. Reinserisci il numero di righe: ");
		scanf("%d", &Righe);
	}
	
	if(Righe>=3){
		Colonne=rand()%21+3;
		printf("Il numero di colonne è %d\n\n", Colonne);
		
		for(i=0; i<Colonne; i++){
			printf("*");
		}
		
		printf("\n");
		
		for(i=0; i<Righe; i++){
			printf("*");
		
			for(j=0; j < (Colonne-2); j++){
				printf("‍‍Q");
			}
			
			printf("*");
			printf("\n");
			
		}
		
		for(i=0; i<Colonne; i++){
			printf("*");
		}
		
		printf("\n");
	}
return 0;
}
