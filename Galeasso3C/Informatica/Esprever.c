/*
Galeasso Federico 3C 13/12/2021 Esercizio pre verifica
Data una serie di numeri (N da 3 a 15) interi random da 10 a 70 (N chiesto all'utente):
A) Stabilire quale numero sia maggiore
Richiesto un nuovo numero N (N da 3 a 15):
A) Far inserire da tastiera all'utente gli N numeri interi (da 30 a 100)
B) Stabilire quale numero sia il minore

Usare funzioni e procedure
+ ChiediNIntero()
+ TrovaMAX()
+ TrovaMIN()

La funzione ChiediNIntero() dovrà essere invocata all'interno delle funzioni TrovaMAX() e TrovaMIN() che restituiranno i risultati che verranno stampati dal main.
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void chiediNIntero();
int TrovaMAX();
void richiediNIntero();
int TrovaMIN();

int main(){
	srand(time(NULL));
	chiediNIntero();
	richiediNIntero();
return 0;
}

void chiediNIntero(){
	int N, i, max, Numero;
	printf("Inserisci un numero intero compreso tra 3 e 15: ");
	scanf("%d", &N);
	while(N<3 || N>15){
		printf("Il numero non è compreso tra 3 e 15, reinseiscilo: ");
		scanf("%d", &N);
	}
	for(i=0; i<N; i++){
		Numero=TrovaMAX();
		if(Numero>max){
			max=Numero;
		}
	}
	printf("Il numero maggiore è %d\n", max);
}

int TrovaMAX(){
	int Numero;
	Numero=rand()%61+10;
	printf("%d\t", Numero);
	printf("\n");
return Numero;
}

void richiediNIntero(){
	int N, i, min=101, Numero;
	printf("Inserisci un numero intero compreso tra 3 e 15: ");
	scanf("%d", &N);
	while(N<3 || N>15){
		printf("Il numero non è compreso tra 3 e 15, reinseiscilo: ");
		scanf("%d", &N);
	}
	for(i=0; i<N; i++){
		Numero=TrovaMIN();
		if(Numero<min){
			min=Numero;
		}
	}
	printf("Il numero minore è %d\n", min);
}

int TrovaMIN(){
	int Numero;
	printf("Inserisci numeri da 3 a 100: ");
		scanf("%d", &Numero);
	while(Numero<3 || Numero>100){
		printf("Inserisci numeri che siano compresi tra 3 e 100: ");
		scanf("%d", &Numero);
	}
return Numero;
}
