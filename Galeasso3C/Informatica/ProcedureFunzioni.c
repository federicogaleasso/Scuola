/*
Galeasso Federico 3C 7/12/2021 Procedure e Funzioni

RIUTILIZZO del codice
PROCEDURA --> non restituisce NULLA al main
FUNZIONE --> restituisce UN valore al main
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// PROTOTIPI
void SommaN();
int Moltiplica();
int ChiediN();
float CalcMedia();

// MAIN
int main(){
	int Risultato, Uno, Due, Tre, Somma=0;
	float Media;
	srand(time(NULL));
	printf("Richiamo la prima volta la procedura\n");
	SommaN(); //  -1- Salta nella PROCEDURA
	printf("Richiamo la seconda volta la procedura\n");
	SommaN(); // -2- Salta di nuovo nella PROCEDURA
	Risultato=Moltiplica(); // -3- Salva il risultato dell'operazione della FUNZIONE dentro a RISULTATO
	printf("%d\n", Risultato); 
	
	Uno=ChiediN();
	Due=ChiediN();
	Tre=ChiediN();
	Somma=Uno+Due+Tre;
	printf("La somma vale %d\n", Somma);
	
	Media=CalcMedia();
	printf("\nLa media vale %.2f\n", Media);
return 0;
}

// Dichiarazione della PROCEDURA
void SommaN(){
	int N, Somma=0, i;
	for(i=0; i<10; i++){
		N=rand()%146+5;
		printf("-%d-\t", N);
		Somma=Somma+N;
	}
	printf("\nLa somma vale %d\n", Somma);
	// -1- Torna al MAIN
	// -2- Torna al MAIN
}

// Dichiarazione della FUNZIONE
int Moltiplica(){
	int N, Moltiplicazione=1, i;
	for(i=0; i<10; i++){
		N=rand()%10+2;
		printf("-%d-\t", N);
		Moltiplicazione=Moltiplicazione*N;
	}
	printf("\nDentro alla funzione la moltiplicazione vale %d\n", Moltiplicazione);
return Moltiplicazione;
// -3- Torna al MAIN e salva il risultato dentro alla variabile RISULTATO
}

// ESERCIZIO
// Creo una FUNZIONE e chiedo all'utente un numero
int ChiediN(){
	int N;
	printf("Inserisci un numero: ");
	scanf("%d", &N);
return N;
}

// ESERCIZIO
// Creo una FUNZIONE e e faccio la media tra 10 numeri random
float CalcMedia(){
	int N, i, Somma=0;
	float Media=0;
	for(i=0; i<10; i++){
	N=rand()%16+10;
	printf("-%d-\t", N);
	Somma=Somma+N;
	}
	Media=(float)Somma/10;
return Media;
}
