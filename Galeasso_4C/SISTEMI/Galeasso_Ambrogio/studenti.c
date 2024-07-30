//GALEASSO FEDERICO 4C 5/1/2023 COMPITO DI NATALE - AMBROGIO - FILE STUDENTI.C

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>
#include <sys/wait.h>

struct sembuf buffer;

void sem_Lock (int, int);
void sem_Unlock (int, int);

int main(){
	system("clear");
	pid_t ChiSono;
	key_t shm_chiave = 1234, sem_chiave = 5678;
	int shm_id, sem_id, N, *dati, i, vassoio, flag = 0, flag_wait;
	
	shm_id = shmget(shm_chiave, sizeof(int)*10, IPC_EXCL | 0666);
	sem_id = semget(sem_chiave, 2, IPC_EXCL | 0666);  
	
	if (shm_id == -1 || sem_id == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	dati = (int *) shmat(shm_id, NULL, 0); 
	
	printf("Inserisci il numero di studenti (tra 20 e 50): ");
	scanf("%d", &N);
	while( N < 20 || N > 50 ){
		printf("ERRORE! Reinserisci il numero di studenti (tra 20 e 50): ");
		scanf("%d", &N);
	}
	
	for(i = 0; i < N; i++){
		if((ChiSono = fork()) < 0){
			printf("Errore nella fork\n");
			exit(-1);
		}
		
		if(ChiSono == 0){
			srand(getpid());
			vassoio = rand()%2;
			while(flag == 0){
				if(semctl(sem_id, vassoio, GETVAL) > 0){
					sem_Lock(sem_id, vassoio);
					printf("PID: %d | Ripiano N°: %d | Posti liberi: %d\n", getpid(), vassoio + 1, semctl(sem_id, vassoio, GETVAL));
					dati[vassoio] += 1;
					flag = 1;
					sleep(2);			
					sem_Unlock(sem_id, vassoio);
				}
			
			}
			exit(1);
		}
	}
	
	for(i = 0; i < N; i++){
		wait(&flag_wait);
	}
	printf("Tutti gli hanno finito di consumare il proprio pasto, Ambrogio può chiudere la mensa.\n");
	
	dati[2] = 0;

	return 0;
}

void sem_Lock (int sem_id, int nVassoio){
    buffer.sem_num=nVassoio;
    buffer.sem_flg=0;
    buffer.sem_op=-1;
    if(semop(sem_id, &buffer, 1) == -1)
        printf("Errore blocco semaforo\n");
}

void sem_Unlock (int sem_id, int nVassoio){
    buffer.sem_num=nVassoio;
    buffer.sem_flg=0;
    buffer.sem_op=1;
    if(semop(sem_id, &buffer, 1) == -1)
        printf("Errore sblocco semaforo\n");
}
