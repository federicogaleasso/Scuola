/*
Galeasso Federico 3C 25/1/2022 Esercizi di recupero
L’Associazione “Amici del Maira” organizza una gara podistica amatoriale a cui partecipano N atleti (con N>0).
Di ogni atleta si sanno:
• Il numero di pettorale (numero inserito in input compreso tra 1 e 50).
• Il genere (“m” o “f”)
• l’età (numero casuale compreso tra 10 e 50)
• Il tempo totale con cui ha terminato la gara (numero casuale compresi tra 80 e 150).

Gestendo l’apposito menu, si chiede di calcolare e visualizzare in output:
0) Esci
1) Quanti (cioè il numero di atlete donne ed il numero di atleti uomini);
2) Vincitore (cioè numero di pettorale ed il tempo dell’atleta vincitore della gara ovvero con il tempo minore);
3) Media tempi (cioè la media dei tempi di tutti gli atleti);
4) Media donne (età media e tempo medio delle atlete donne);
5) Ultimo (cioè Il numero di pettorale ed il tempo dell’atleta ultimo classificato ovvero con il tempo maggiore).
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Prototipi
void nAt();
void pet();

int creaRandom(int);
void quanti();
void vinc();
void mediaT();
void mediaD();
void ultimo();

int main(){
	int errore=0, menu, N, nPet, i, piu=0, eta, tGara, contm=0, contf=0;
	char genere=' ';
	srand(time(NULL));
	nAt();
	
	for(i=0; i<N; i++){
		pet();
		
		printf("Inserisci il genere dell'atleta %d (m - f) --> ", piu);
		scanf("%c", &genere);
		while(getchar()!='\n');
		while(genere=='m' || genere=='f'){
			printf("Inserisci il genere dell'atleta %d (m - f) --> ", piu);
			scanf("%c", &genere);
			while(getchar()!='\n');
		}
		if(genere=='m'){
			contm++;
		} else{
			contf++;
		}
		
		eta=rand()%41+10;
		printf("L'età dell'atleta %d è --> %d\n", piu, eta);
		
		tGara=rand()%71+80;
		printf("L'età dell'atleta %d è --> %d\n", piu, tGara);
	}
	
	printf("Inserisci 0 - 1 - 2 - 3 - 4 - 5 --> ");
	scanf("%d", &menu);
	while(errore==0){
		switch(menu){
			case 0:
				errore=1;
				printf("Ciao!\n");
			break;
			case 1:
				//quanti();
			break;
			case 2:
				//vinc();
			break;
			case 3:
				//mediaT();
			break;
			case 4:
				//mediaD();
			break;
			case 5:
				//ultimo();
			break;
			default:
				errore=1;
				printf("Scelta non valida!\n");
		}
	}
return 0;
}

void nAt(){
	int errore=0, menu, N, nPet, i, piu=0, eta, tGara, contm=0, contf=0;
	char genere=' ';
	printf("Inserisci il numero di atleti (MAGGIORE di 0!) --> ");
	scanf("%d", &N);
	
	while(N<=0){
		printf("Inserisci il numero di atleti (MAGGIORE di 0!) --> ");
		scanf("%d", &N);
	}
}

void pet(){
	int errore=0, menu, N, nPet, i, piu=0, eta, tGara, contm=0, contf=0;
	char genere=' ';
	piu++;
	printf("Inserisci il numero del pettorale dell'atleta %d (TRA 1 e 50!) --> ", piu);
	scanf("%d", &nPet);
	while(nPet<1 || nPet>50){
		printf("Inserisci il numero del pettorale dell'atleta %d (TRA 1 e 50!) --> ", piu);
		scanf("%d", &nPet);
	}
}
