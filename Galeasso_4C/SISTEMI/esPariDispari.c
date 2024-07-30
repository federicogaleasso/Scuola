/*
GALEASSO FEDERICO 4C 27/9/22 ES IN CLASSE - PARI DISPARI

Il processo padre genera N figli
Ogni figlio genera un numero casuale compreso tra 5 e 17
Se il numero generato è pari, il figlio lo stampa a video e termina
Il padre esegue il conteggio dei figli dispari e lo visualizza a video
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int figli, i, numero, stato_wait, min=5, max=17, somma=0, numeroDispari=0;

	printf("Quanti figli vuoi generare? --> ");
	scanf("%d", &figli);

	for(i=0; i<figli; i++){
	//INIZIO codice di TUTTI i FIGLI
		if((ChiSono=fork())<0){
			printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
			exit(-1);
		}
		
		if(ChiSono==0){
			srand(getpid());
			numero=rand()%(max-min+1)+min;
			//controllo se il numero è pari
			if(numero%2==0){
				printf("Figlio: %d | Numero: %d\n", getpid(), numero);
			}
			exit(numero);
		}
	}
	//FINE codice di TUTTI i FIGLI

	//INIZIO codice processo PADRE
	for(i=0; i<figli; i++){
		pid=wait(&stato_wait);
		stato_wait=stato_wait/256;
		if(stato_wait%2!=0){
			numeroDispari++;
		}
		printf("Figlio %d terminato!\n", pid);
	}
	//FINE codice processo PADRE
	printf("I numeri dispari sono: %d\n", numeroDispari);

return 0;
}
