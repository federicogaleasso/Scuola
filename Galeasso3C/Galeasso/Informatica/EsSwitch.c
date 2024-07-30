/*
Galeasso Federico 3C 11/11/2021
Creare un programma che simuli una calcolatrice, richiedendo due numeri e un operatore. Partendo dall'esercizio della calcolatrice fare in modo che vengano richiesti a ciclo continuo due nuovi numeri e l'operatore, finchè l'operatore non è zero. In tal caso il programma termina
1=Somma
2=Sottrazione
3=Moltiplicazione
4=Divisione
*/
#include <stdio.h>
int main (){
	int N1, N2, Operatore, Errore=0;
	float Risultato=0.0;
	while(Operatore!=0){
	printf("Inserisci il primo numero: ");
	scanf("%d", &N1);
	printf("Inserisci il primo numero: ");
	scanf("%d", &N2);
	printf("Inserisci l'operatore: \n1=Somma\n2=Sottrazione\n3=Moltiplicazione\n4=Divisione\nInserire 0 per terminare.\n");
	scanf("%d", &Operatore);
	if(Operatore==0){
		printf("Programma terminato!\n");
		Errore=1;
	}
	switch(Operatore){
		case 1:
		Risultato=N1+N2;
		break;
		case 2:
		Risultato=N1-N2;
		break;
		case 3:
		Risultato=N1*N2;
		break;
		case 4:
		if(N2==0){
			printf("Divisione impossibile\n");
			Errore=1;		
		}
		else{
			Risultato=(float)N1/N2;
		}
		break;
		default:
		if(Operatore < 0 || Operatore > 4){
		printf("Hai scelto un'operatore non valido!\n");
		Errore=1;
		}
		}
	if(Errore==0){
		printf("Il risultato di %d e %d è %.2f\n", N1, N2, Risultato);
	}
	}
return 0;
}
