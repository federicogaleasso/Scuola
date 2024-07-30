//GALEASSO FEDERICO 4C 29/11/2022 ESERCIZIO SHM-SEMAFORI - FILE ELFO (LETTORE)

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
	int shmid, semid, sem_stato, *dati, N, i=0, flag = 0;
	
	shmid = shmget(keyshm, SHM_SIZE, 0666);
	semid = semget(keysem, 1, 0666);
	
	printf("Benvenuto!\n");
	
	if((shmid ==-1) || (semid==-1)){
		printf("Errore nella creazione della memoria o del semaforo\n");
		exit(-1);
	}
	
	sem_stato=semctl(semid, 0, SETVAL, 1);
	dati=(int *)shmat(shmid, NULL, 0);
	
	while (flag == 0) {
		if (dati[0] != 0) {
			N = dati[0];
			flag = 1;
		}
	}
	
	FILE *fp;
	fp = fopen("lista.txt", "w");
	while (i < N) {
		if(semctl(semid, 0, GETVAL)==1) {
			semLock(semid);
			printf("Il numero del regalo è %d", dati[i+1]);
			semUnlock(semid);
			fprintf(fp, "Il PID è %d | Il numero del regalo è %d\n\n", getpid(), dati[i+1]);
			i++;
		}
	}
	fclose(fp);
	
	dati[0] = 0;
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
