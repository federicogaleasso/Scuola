//GALEASSO FEDERICO 4C 5/1/2023 COMPITO DI NATALE - AMBROGIO - FILE AMBROGIO.C

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>
#include <sys/wait.h>

struct sembuf buffer;

int main(){
	system("clear");
	key_t shmChiave = 1234, semChiave = 5678;
	int shm_id, sem_id, i, sem_stato, *dati;
	
	shm_id = shmget(shmChiave, sizeof(int)*10 , 0666 | IPC_CREAT); 
	sem_id = semget(semChiave, 2, 0666 | IPC_CREAT);         
  
	if (shm_id == -1 || sem_id == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	for (i = 0; i < 2; i++){
		sem_stato = semctl(sem_id, i, SETVAL, 5);
	}
	
	dati = (int *) shmat(shm_id, NULL,0);
	
	for (i = 0;i < 5; i++){
		dati[i] = 0;
	}
	
	printf("Benvenuto, la mensa è aperta!\n");
	dati[2] = 1;
	
	while(dati[2] != 0){
		printf("Sto aspettando che tutti gli studenti finiscano di consumare il proprio pasto...\n");
		sleep(3);
	}
	
	printf("Tutti gli studenti hanno finito di consumare il proprio pasto.\n");
	
	shmctl(shm_id, IPC_RMID, NULL);
	
	for(i = 0; i < 2; i++){
		semctl(sem_id, i, IPC_RMID, 0);
	}
	printf("Ho chiuso la mensa, arrivederci!\n");
	return 0;
}
