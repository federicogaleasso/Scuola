//Galeasso Federico 3C Correzione verifica

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int NumeroRandom(int, int);
void LancioDadi();

int main (void){
	int Massimo=6, Minimo=1, ERROR=0;
	char Menu;
	srand(time(NULL));
	printf("A - B - C - E --> ");
	scanf("%c", &Menu);
	while(getchar()!='\n');
	if(Menu=='E' || Menu=='e'){
		ERROR=ERROR+1;
	}
	if(ERROR==0){
		switch(Menu){
			case 'A':
			case 'a':
				LancioDadi();
			break;
			case 'B':
			case 'b':
			break;
			case 'C':
			case 'c':
			break;
			default:
				printf("Lettera non valida!\n");
		}
	}
return 0;
}

int NumeroRandom(int Massimo, int Minimo){
return rand()%(Massimo-Minimo+1)+Minimo;
}

void LancioDadi(){
		int i, NPart=0, DADOUTENTE, DADO2UTENTE, DADO2PC, DADOPC, SPC, SUT, Massimo, Minimo;
		printf("Inserisci il numero di partite: ");
		scanf("%d", &NPart);
		while(NPart>10 || NPart<1){
			printf("Inserisci il numero di partite tra 1 e 10: ");
			scanf("%d", &NPart);
		for(i=0; i<NPart; i++){
			DADOPC=NumeroRandom(6, 1);
			DADOUTENTE=NumeroRandom(6, 1);
			DADO2PC=NumeroRandom(6, 1);
			DADO2UTENTE=NumeroRandom(6, 1);
			SPC=DADO2PC+DADOPC;
			SUT=DADOUTENTE+DADO2UTENTE;
			printf("Comp:%d %d\nUt: %d %d\nSomma computer: %d\nSomma ut: %d\n",DADOPC , DADO2PC , DADOUTENTE, DADO2UTENTE, SPC, SUT);
			if(SPC==SUT){
				printf("Pari\n");
			}
			else{
				if(SPC>SUT){
					printf("Computer\n");
				}
				else{
					printf("Utente\n");
				}
			}
		
		}
}
