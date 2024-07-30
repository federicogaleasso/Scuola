//GALEASSO FEDERICO 4C 13/9/22 PRIMO ESERCIZIO PROCESSI
//Eseguire una fork e stampare il PID del padre e del figlio.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>	//gestione processi

int main(){
	pid_t ChiSono;	//pid_t è un nuovo  tipo di variabile. Dopo la fork, in ChiSono ci sarà il valore di ritorno
	
	ChiSono=fork();
	
	if(ChiSono<0){
		printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
		exit(-1);	//conclude il processo con un valore negativo
	}
	
	if(ChiSono==0){
		//codice PROCESSO FIGLIO
		printf("Sono il processo FIGLIO, il mio PID è %d. Il PID del processo PADRE è %d\n", getpid(), getppid()); //getpid() --> funzione che stampa il PID del processo. getppid() --> stampa il processo del PADRE del processo
	} else{
		printf("Sono il processo PADRE, il mio PID è %d. Il PID del mio processo PADRE è %d\n", getpid(), getppid());
	}
	
return 0;
}
