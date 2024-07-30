//GALEASSO FEDERICO 4C 20/9/22 QUARTO ESERCIZIO PROCESSI - GENERAZIONE DI N FIGLI
//Il processo PADRE genera N figli e li aspetta

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int figli, i, numero, stato_wait;
	
	printf("Inserisci un numero: ");
	scanf("%d", &numero);
	
	printf("Quanti figli vuoi generare? --> ");
	scanf("%d", &figli);
	
	for(i=0; i<figli; i++){
	//INIZIO codice di TUTTI i FIGLI
		if((ChiSono=fork())<0){
			printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
			exit(-1);
		}
		
		if(ChiSono==0){
			srand(getpid()); //utilizziamo come srand la getpid(), perchè se usassimo il time NULL il numero sarebbe uguale per tutti i figli. Il PID è l'unica cosa che differenzia un processo da unn'altro
			numero=numero+rand()%21;
			printf("Figlio: %d | Numero: %d\n", getpid(), numero);
			exit(numero);
		}
	}
	//FINE codice di TUTTI i FIGLI
	
	//INIZIO codice processo PADRE
	for(i=0; i<figli; i++){
		pid=wait(&stato_wait);
		printf("Figlio %d terminato!\n", pid);
	}
	printf("Numero alla fine del programma: %d\n", numero);
	//FINE codice processo PADRE

return 0;
}
