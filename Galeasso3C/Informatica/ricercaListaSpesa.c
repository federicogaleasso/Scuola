/*
Galeasso Federico 3C 23/3/2022 Eserczio Lista Spesa (vettori e ricerca)

In un negozio viene fatta una spesa dall'utente che acquista N prodotti (N viene stabilito da un inserimento ciclico dei prezzi dei prodotti fino a quando non viene inserito il prezzo 0 o raggiunto il numero di 20 articoli) dei quali viene richiesto il prezzo in input e memorizzato nell'opportuno vettori prezziA.

I prodotti sono semplicemente numerati da 1 a N.

Aquisiti tutti i prezzi:

+ stampare la lista dei prezzi con i nomi (numeri) dei relativi prodotti
+ ordinare la lista dei prodotti dal prezzo più basso al più caro
+ stampare la nuova lista ordinata con i CORRETTI nomi (numeri) dei relativi prodotti
+ cercare un prezzo richiesto in input all'utente rispondendo con:
"non esiste un prodotto con quel prezzo!" (se non è stato trovato)
"il prodotto X ha il prezzo cercato!" (X è il nome, cioè il numero, del prodotto se è strato trovato)
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 20

//Prototipi
int creaRandom(int, int);
void caricaVet(int[]);
void stampaVet(int[], int[]);
void bubbleSort(int[], int[]);

int main(){
	int prezziA[MAX], prod[MAX];
	srand(time(NULL));
	system("clear");
	caricaVet(prezziA);
	stampaVet(prezziA, prod);
	bubbleSort(prezziA, prod);
	printf("Ordino...\n");
	stampaVet(prezziA, prod);
return 0;
}

int creaRandom (int min, int max) {
	return rand()%(max-min+1)+min;
}

void caricaVet(int prezziA[]){
	int i=0, flag=0;
	while(flag==0 && i<20){
		printf("Prezzo %d prodotto(0 per uscire, massimo 20): ", i+1);
		scanf("%d", &prezziA[i]);
		if(prezziA[i] == 0){
			flag=1;
		}
		i++;
	}
}
void stampaVet(int prezziA[], int prod[]) {
	int i=0;
	for (i=0; i<=prezziA[i]; i++) {
		printf("Prodotto %d | Prezzo: %d\n\n", prod[i+1], prezziA[i]);
	}
}


void bubbleSort (int prezziA[], int prod[]) {
	int temp, i=0, j=0, flag=1;
	j=5;
	flag=1; //1 vero 0 falso
	while (flag == 1) {
		flag=0;
		for (i=0; i<j-1; i++) {
			if (prezziA[i] > prezziA[i+1]) {
				temp = prezziA[i];
				prezziA[i] = prezziA[i+1];
				prezziA[i+1] = temp;
				
				temp = prod[i];
				prod[i] = prod[i+1];
				prod[i+1] = temp;
				flag=1;
			}
		}
		j=j-1;
	}
}
