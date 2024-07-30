//Galeasso Federico 3C 22/3/2022 Eserczio Ricerca Dicotomica

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 5

//Prototipi
void caricaVet(int []);
void stampaVett(int []);
void bubbleSort(int []);
int ricercaDicotomica(int []);
int creaRandom(int, int);

int main () {
	int vettore[MAX], trovato=0;
	char invio=' ';
	srand(time(NULL));
	
	system("clear");
	printf("\e[1;35m*** BENVENUTO ***\e[0;37m");
	printf("\n");
	printf("\n");
	printf("\e[1;36mPremi invio per cominciare...\e[0;37m");
	scanf("%c", &invio);
	printf("\n");
	caricaVet(vettore);
	printf("\e[1;33m-- Stampo \e[1;34m5\e[0;37m \e[1;33mnumeri non ordinati--\e[0;37m\n\n");
	stampaVett(vettore);
	printf("\n");
	printf("\e[1;36mPremi invio per entrare nel \e[1;34mBUBBLE SORT\e[0;37m\e[1;36m e per stampare i numeri ordinati...\e[0;37m");
	scanf("%c", &invio);
	bubbleSort(vettore);
	printf("\n");
	printf("\e[1;33m-- Ristampo i \e[1;34m5\e[0;37m \e[1;33mnumeri ordinati --\e[0;37m\n\n");
	stampaVett(vettore);
	trovato=ricercaDicotomica(vettore);
	if (trovato != -1) {
		printf("\e[1;32mNUMERO TROVATO!\e[0;37m \e[1;33mIl numero è presente nella posizone \e[1;32m%d\e[0;37m \e[1;33mdel vettore\e[0;37m\n\n", trovato);
	} else {
		printf("\e[1;31mNUMERO NON TROVATO!\e[0;37m \e[1;33mIl numero non è presente nel vettore\e[0;37m\n\n");
	}
	printf("\e[1;35m*** ARRIVEDERCI! ***\e[0;37m\n\n");
return 0;
}

int creaRandom (int min, int max) {
	return rand()%(max-min+1)+min;
}

void caricaVet (int vettore[]) {
	int i=0;
	for (i=0; i<MAX; i++) {
		vettore[i]=creaRandom(1, 50);
	}
}

void stampaVett (int vettore[]) {
	int i=0;
	for (i=0; i<MAX; i++) {
		printf("\e[1;36m------------\e[0;37m\n");
		printf("\e[1;37mNumero \e[1;34m%d\e[0;37m\e[1;37m:\e[0;37m\e[0;37m \e[1;33m%d\e[0;37m\n", i+1, vettore[i]);
	}
	printf("\e[1;36m------------\e[0;37m\n");
}

void bubbleSort (int vettore[]) {
	int temp, i=0, j=0, flag=1;
	j=5;
	flag=1; //1 vero 0 falso
	while (flag == 1) {
		flag=0;
		for (i=0; i<j-1; i++) {
			if (vettore[i] > vettore[i+1]) {
				temp = vettore[i];
				vettore[i] = vettore[i+1];
				vettore[i+1] = temp;
				flag=1;
			}
		}
		j=j-1;
	}
}

int ricercaDicotomica (int vettore[]) {
	int i=0, j=0, k=0, trovato=-1, pos=0;
	j=5-1;
	printf("\n");
	printf("\e[1;33mInserisci un \e[1;34mnumero\e[0;37m \e[1;33me verrà ricercato nel vettore precendentemente stampato. Ti faremo sapere se verrà trovato! --> \e[0;37m");
	scanf("%d", &k);
	printf("\n");
	while (i <= j && trovato == -1) {
		pos=(i+j)/2;
		if (vettore[pos] == k) {
			trovato=pos;
		} else if (vettore[pos] > k) {
			j=pos-1;
		} else {
			i=pos+1;
		}
	}
return trovato;
}
