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
	char *dati, stringa[50];
	
	//CREO LA MEMORIA
	
	shmid=shmget(chiave, DIM, 0666 | IPC_CREAT);
	
	if(shmid==-1){
		printf("Errore nella creazione della memoria condivisa\n");
		exit(-1);
	}
	
	//MI AGGANCIO ALLA MEMORIA
	
	dati=(char *)shmat(shmid, NULL, 0);
	
	if(dati==(char *)-1){
		printf("Errore nella shmat\n");
		exit(-2);
	}
	
	printf("Inserisci una stringa: ");
	//scanf("%s", stringa);
	gets(stringa);
	
	//COPIO LA STRINGA NELLA MEMORIA
	
	strcpy(dati, stringa);
	
	while(strcmp(stringa, "fine")!=0){
	
		printf("Inserisci una stringa: ");
		//scanf("%s", stringa);
		gets(stringa);
		
		//COPIO LA STRINGA NELLA MEMORIA
		
		strcpy(dati, stringa);
		
	}
	
	printf("Hai scelto di smettere\n");
	
	while(strcmp(dati,"chiudi")!=0){
		sleep(2);
	}
	
	//DISTRUGGO LA MEMORIA
	
	printf("Il lettore ha finito, distruggo la memoria\n");
	
	shmctl(shmid, IPC_RMID, NULL);
	
	printf("Memoria distrutta\n");
return 0;
}
