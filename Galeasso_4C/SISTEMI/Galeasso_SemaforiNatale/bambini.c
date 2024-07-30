//GALEASSO FEDERICO 4C 29/11/2022 ESERCIZIO SHM-SEMAFORI - FILE BAMBINI (SCRITTORE)

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

#define SHM_SIZE 1024

struct sembuf buffer;

void semLock(int);
void semUnlock(int);

int main() {

	system("clear");
		
	key_t keyshm = 1234, keysem = 5678;
	int shmid, semid, sem_stato, regalo=0, *dati, i = 0, N = 0, num=0;
	
	shmid = shmget(keyshm, SHM_SIZE, 0666 | IPC_CREAT);
	semid = semget(keysem, 1, 0666 | IPC_CREAT);
	
	if((shmid ==-1) || (semid==-1)){
		printf("Errore nella creazione della memoria o del semaforo\n");
		exit(-1);
	}
	
	sem_stato=semctl(semid, 0, SETVAL, 1);
	dati=(int *)shmat(shmid, NULL, 0);
	
	dati[0] = 0;
	
	printf("Inserisci il numero di bambini: ");
	scanf("%d", &num);
	
	dati[0] = num;
	while ( i < num )  {
		if(semctl(semid, 0, GETVAL)==1) {
			semLock(semid);
			printf("Inserisci il numero del regalo: ");
			scanf("%d", &regalo);
			dati[i+1] = regalo;
			semUnlock(semid);
			i = i + 1;
		}	
	}
	
	if (dati[0] == 0) {
		shmctl(shmid, IPC_RMID, NULL);
		sem_stato=semctl(semid, 0, IPC_RMID, 0);
	}
return 0;
}

void semLock(int id){
	buffer.sem_num=0;
	buffer.sem_flg=0;
	buffer.sem_op=-1;
	if(semop(id, &buffer, 1)==-1){
		printf("Errore blocco del semaforo\n");
	} else {
		printf("\nSemaforo bloccato\n");
	}
}


void semUnlock(int id){
	buffer.sem_num=0;
	buffer.sem_flg=0;
	buffer.sem_op=1;
	if(semop(id, &buffer, 1)==-1){
		printf("Errore sblocco del semaforo\n");
	} else {
		printf("\nSemaforo sbloccato\n");
	}
}
