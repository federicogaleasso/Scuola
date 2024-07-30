/*
GALEASSO FEDERICO 4C 30/9/22 COMPITO NUMERO MAGGIORE E MINORE

Scrivere un programma che permetta al processo padre di generare N figli.
Ogni figlio genera un numero casuale compreso tra 7 e 29.
Il padre deve stampare a video il PID del figlio che ha generato il numero maggiore ed il PID del figlio che ha generato il numero minore.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int figli, i, numero, stato_wait, min=7, max=29, somma=0, nMax=0, pidMax=0, nMin=29, pidMin=0;

	printf("Quanti figli vuoi generare? --> ");
	scanf("%d", &figli);

	//INIZIO codice di TUTTI i FIGLI
	for(i=0; i<figli; i++){
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
		pid=wait(&stato_wait);
		stato_wait=(stato_wait/256);
		if(stato_wait>nMax){
			nMax=stato_wait;
			pidMax=getpid();
		}
		if(stato_wait<nMin){
			nMin=stato_wait;
			pidMin=getpid();
		}
		printf("Figlio %d terminato!\n", pid);
	}
	//FINE codice processo PADRE
	printf("Il PID del figlio con il numero maggiore (%d) è: %d\n", nMax, pidMax);
	printf("Il PID del figlio con il numero minore (%d) è: %d\n", nMin, pidMin);

return 0;
}
