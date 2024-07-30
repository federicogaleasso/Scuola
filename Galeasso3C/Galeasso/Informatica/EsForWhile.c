/*
Galeasso Federico 3C
Esercizio
Creare un programma che richieda l’inserimento di N studenti (N compreso tra 4 e26). Per ogni studente viene richiesta l’altezza. L’altezza deve essere UN numerorandom compreso tra 150 e 182 oppure tra 190 e 201, estremi tutti compresi (nb: ilnumero estratto deve essere uno preso tra i due intervalli indicati). Contare estampare in output il numero di studenti che hanno un’altezza compresa tra 150 e 182cm ed il numero di studenti che hanno un’altezza compresa tra 190 e 201. Stampareinoltre in output quale dei due conteggi è maggiore.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

	int Numero = 0, Altezza = 0, Bassi = 0, Alti = 0, I = 0, Valore = 0;
	srand(time(NULL));
	
	printf("inserisci il numero di studenti ");
	scanf("%d", &Numero);
	
	while (Numero < 4 || Numero > 26){
		printf("il numero inserito è minore di 4 o maggiore di 26 \n");
		printf("inserisci il numero di studenti ");
		scanf("%d", &Numero);
	}
	
	for (I = 0;I < Numero;I = I +1){
		Valore = rand()%2;
		if (Valore == 0){
			Altezza = (rand()%33 + 150);
		}
		else {
			Altezza = (rand()%12 + 190);
		}
		if (Altezza < 183){
			Bassi = (Bassi + 1);
		}
		else {
			Alti = (Alti + 1);
		}
	}
	
	printf("il numero degli studenti alti fra i 150 e 182 è di: %d \n", Bassi);
	printf("il numero degli studenti alti fra i 190 e 201 è di: %d \n", Alti);
	
	if(Bassi==Alti){
		printf("ci sono tanti studenti alti quanti bassi \n");
	} else {
		if (Bassi > Alti){
			printf("ci sono piu studenti alti tra i 150 e i 182 \n");
		}
		else {
			printf("ci sono piu studenti alti tra i 190 e i 201 \n");
		}
	}

return 0;
}
