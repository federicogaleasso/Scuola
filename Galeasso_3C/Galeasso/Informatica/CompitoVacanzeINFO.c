// Galeasso Federico 3C Compito delle vacanze natalizie (CALCOLATRICE)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void Menu();
void somma(int);
void sottrazione(int);
void moltiplicazione(int);
void divisione(int);

int main(){
	Menu();
return 0;
}

void Menu() {
	int s;
	char Menu;
	printf("Benvenuto nella | CALCOLATRICE |\n\n");
	printf("Somma 👉️ +\nSottrazione 👉️ -\nMoltiplicazione 👉️ *\nDivisione 👉️ /\n\n");
	printf("Inserisci qui l'operatore ➡️   ");
	scanf("%c", &Menu);
	while(getchar()!='\n'){};
	switch (Menu) {
		case '+':
			somma(s);
		break;
		case '-':
			sottrazione(s);
		break;
		case '*':
			moltiplicazione(s);
		break;
		case '/':
			divisione(s);
		break;
		default:
			printf("Operatore non valido!\n");
	
	}
}

void sottrazione (int s) {
	int N1, N2, SOTTRAZIONE;
	printf("Inserisci il primo numero: ");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: ");
	scanf("%d", &N2);
	SOTTRAZIONE= N1-N2;
	printf("La sottrazione vale %d\n", SOTTRAZIONE);
}

void somma(int s) {
	int N1, N2, SOMMA;
	printf("Inserisci il primo numero: ");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: ");
	scanf("%d", &N2);
	SOMMA=N1+N2;
	printf("La somma vale %d\n", SOMMA);
}

void divisione (int s) {
	int N1, N2; 
	float DIVISIONE;
	printf("Inserisci il primo numero: ");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: ");
	scanf("%d", &N2);
	if (N2!=0) {
		DIVISIONE= (float)N1/N2;
		printf("La divisione vale %.2f\n", DIVISIONE);
	} else {
		printf("IMPOSSIBILE!!!\n");
	}
}

void moltiplicazione (int s) {
	int N1, N2, MOLTIPLICAZIONE;
	printf("Inserisci il primo numero: ");
	scanf("%d", &N1);
	printf("Inserisci il secondo numero: ");
	scanf("%d", &N2);
	MOLTIPLICAZIONE= N1*N2;
	printf("La moltiplicazione vale %d\n", MOLTIPLICAZIONE);
}
