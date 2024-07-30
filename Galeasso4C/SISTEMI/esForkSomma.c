/*
GALEASSO FEDERICO 4C 23/9/22 COMPITO FORK SOMMA

Il processo padre crea N figli, ognuno dei quali genera un numero casuale compreso tra 1 e 50. Il padre, dopo aver aspettato la fine di tutti i figli, deve sommare i numeri generati e dare il risultato della somma in putput
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int figli, i, numero, stato_wait, min=1, max=50, somma=0;

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
			printf("Figlio: %d | Numero: %d\n", getpid(), numero);
			exit(numero);
		}
	}
	//FINE codice di TUTTI i FIGLI

	//INIZIO codice processo PADRE
	for(i=0; i<figli; i++){
		pid=wait(&stato_wait);	//stato_wait contiene il valore di ritorno della exit(), ovvero il numero
		somma=somma+(stato_wait/256);	//dobbiamo quindi sommare somma con stato_wait. stato_wait lo dividiamo per 256 (ovvero 8 posizioni) per spostare il numero nella cifra più significativa
		printf("Figlio %d terminato!\n", pid);
	}
	//FINE codice processo PADRE
	printf("La somma di tutti i numeri è: %d\n", somma);

return 0;
}
