//GALEASSO FEDERICO 4C 20/9/22 TERZO ESERCIZIO PROCESSI
//Modifica dell'esercizio SecondaFork.c con attesa del padre

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>	//gestisce l'attesa del PADRE

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int numero=42, stato_wait;
	
	printf("Numero iniziale: %d\n", numero);
	
	if((ChiSono=fork())<0){
		printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
		exit(-1);
	}
	
	//INIZIO codice processo FIGLIO
	if(ChiSono==0){
		numero=numero*3;
		printf("Figlio: %d | Numero: %d\n", getpid(), numero);
		exit(1);
	}
	//FINE codice processo FIGLIO
	
	//INIZIO codice processo PADRE
	pid=wait(&stato_wait);	//contiene il valore di ritorno della exit, quindi il numero 1. In più punta alla cella di memoria della exit e restuisce il pid del processo
	printf("Sono il processo PADRE con PID %d. Processo FIGLIO %d terminato!\n", getpid(), pid);
	printf("Numero alla fine del programma: %d\n", numero);
	//FINE codice processo PADRE

return 0;
}
