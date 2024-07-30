//Galeasso Federico 3C 15/2/2022 Verifica POTENZIAMENTO

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
int creaRandom(int, int);
void gioco();
//void giocataPC();
//void confronto();

int main(){
	int n=0, i=0, piu=1, exit=0, sino=0;
	srand(time(NULL));
	while(exit==0){
		printf("Inserisci il numero di partite (>=3, <=12) --> ");
		scanf("%d", &n);
		while(n<3 || n>12){
			printf("Inserisci il numero di partite (>=3, <=12)--> ");
			scanf("%d", &n);
		}
		for(i=0; i<n; i++){
			printf("%d° ROUND\n", piu++);
			gioco();
			//giocataPC();
			//confronto();
		}
		printf("Vuoi continuare? [1-si/0-no] --> ");
		scanf("%d", &sino);
		if(sino==0){
			exit=1;
			printf("Ciao ciao!\n");
		}
	}
return 0;
}

int creaRandom(int max, int min){
return rand()%(max-min+1)+min;
}

void gioco(){
	int semeutente=0, ncartautente=0, semepc=0, ncartapc=0, vinteutente=0, perseutente=0, vintepc=0, persepc=0, VITTORIA=0, PERSE=0;
	
	//utente
	printf("Inserisci il seme della carta (1-picche, 2-fiori, 3-quadri, 4-cuori) --> ");
	scanf("%d", &semeutente);
	ncartautente=creaRandom(10,1);
	printf("Il numero della carta scelta dall'utente è --> %d\n", ncartautente);
	
	//pc
	semepc=creaRandom(4,1);
	printf("Ecco il seme della carta scelta dal PC (1-picche, 2-fiori, 3-quadri, 4-cuori) --> %d\n", semepc);
	ncartapc=creaRandom(10,1);
	printf("Il numero della carta scelta dal PC è --> %d\n", ncartapc);
	
	//controlli
	if(semeutente==4 && semepc==4 && ncartautente==ncartapc || semeutente==3 && semepc==3 && ncartautente==ncartapc || semeutente==2&& semepc==2 && ncartautente==ncartapc || semeutente==1 && semepc==1 && ncartautente==ncartapc){
		printf("Pareggio!");
		vinteutente=vinteutente+1;
		vintepc=vintepc+1;
	}
	if(semeutente==4 && semepc==3){ //cuori vince su quadri
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
		VITTORIA=VITTORIA+1;
	}
	if(semeutente==3 && semepc==1){ //quandri vince su picche
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
		VITTORIA=VITTORIA+1;
	}
	if(semeutente==2 && semepc==4){ //fiori vince su cuori
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
		VITTORIA=VITTORIA+1;
	}
	if(semeutente==1 && semepc==2){ //picche vince su fiori
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
		VITTORIA=VITTORIA+1;
	}
	if(semeutente==4 && semepc==2){
		printf("Hai perso!\n");
		perseutente=perseutente+1;
		PERSE=PERSE+1;
	}
	if(semeutente==3 && semepc==4){
		printf("Hai perso!\n");
		perseutente=perseutente+1;
		PERSE=PERSE+1;
	}
	if(semeutente==2 && semepc==1){
		printf("Hai perso!\n");
		perseutente=perseutente+1;
		PERSE=PERSE+1;
	}
	if(semeutente==1 && semepc==3){
		printf("Hai perso!\n");
		perseutente=perseutente+1;
		PERSE=PERSE+1;
	}
	printf("Punteggio utente --> %d\n", vinteutente);
	printf("VITTORIE utente --> %d\n", VITTORIA);
	printf("PERSE utente --> %d\n", PERSE);
}

/*void giocataPC(){
	int semepc=0, ncartapc=0;
	semepc=creaRandom(4,1);
	printf("Ecco il seme della carta scelta dal PC (1-picche, 2-fiori, 3-quadri, 4-cuori) --> %d\n", semepc);
	ncartapc=creaRandom(10,1);
	printf("Il numero della carta scelta dal PC è --> %d\n", ncartapc);
}

void confronto(){
	int vinteutente=0, perseutente=0, pareggio=0;
	if(semeutente==4 && semepc==4 && ncartautente==ncartapc){
		printf("Pareggio!");
		pareggio=pareggio+1;
	}
	if(semeutente==4 && semepc==3){ //cuori vince su quadri
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
	}
	if(semeutente==3 && semepc==1){ //quandri vince su picche
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
	}
	if(semeutente==2 && semepc==4){ //fiori vince su cuori
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
	}
	if(semeutente==1 && semepc==2){ //picche vince su fiori
		printf("Hai vinto!\n");
		vinteutente=vinteutente+3;
	}
}
*/
