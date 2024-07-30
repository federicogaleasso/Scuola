//GALEASSO FEDERICO 4C 15/11/2022 ESERCIZIO SULLA MEMORIA CONDIVISA + FUNZIONE SCRITTORE E LETTORE CON STRINGHE SU 2 FILE

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <string.h>

#define DIM 1024

int main(){
	key_t chiave=1234;
	int shmid;
	char *dati;
	
	//CREAZIONE ID MEMORIA
	
	shmid=shmget(chiave, DIM, 0666);
	
	if(shmid==-1){
		printf("Errore nella shmget\n");
		exit(-1);
	}
	
	//MI AGGANCIO ALLA MEMORIA
	
	dati=(char *)shmat(shmid, NULL, 0);
	
	printf("Leggo la stringa\n");
	printf("%s\n", dati);
	
	while(strcmp(dati,"fine")!=0){
		printf("%s\n", dati);
	}
	
	printf("Puoi chiudere\n");
	sleep(4);
	strcpy(dati,"chiudi");
return 0;
}
