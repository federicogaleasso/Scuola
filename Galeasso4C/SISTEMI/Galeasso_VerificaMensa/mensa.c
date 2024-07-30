//LETTORE

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>

#define SHM_SIZE 1024
struct sembuf buffer;

void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);

int main(){
	system("clear");
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, sem_stato, *dati, flag2=0, i;
	
	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666 | IPC_CREAT);
	sem_id = semget(sem_chiave, 1, 0666 | IPC_CREAT);        
  
	if (shm_id == -1 || sem_id == -1){
  		printf("Errore nella gestione della memoria o dei semafori\n");
    	exit(-1);
  	}
	sem_stato=semctl(sem_id, 0, SETVAL,1);
	
	dati=(int *) shmat(shm_id, NULL,0);
	
	while(flag2==0){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			if(dati[0]!=0){
				flag2=1;
				for(i=1;i<=(dati[0]*2);i=i+2){
					if(dati[i+1]==0){
						printf("Commensale: %d | Tavolo: %d (menu a base di pesce)\n ", dati[i],dati[i+1]);
					}
					if(dati[i+1]==1){
						printf("Commensale: %d | Tavolo: %d (menu a base di carne)\n ", dati[i],dati[i+1]);
					}
					if(dati[i+1]==2){
						printf("Commensale: %d | Tavolo: %d (menu vegetariano)\n ", dati[i],dati[i+1]);
					}
				}
				printf("Tutti i commensali hanno hanno mangiato\n");
			}else{
				printf("I commensali stanno scegliendo il loro tavolo\n");
				sleep(2);
			}
			sem_Unlock(sem_id);
		}	
	}
	shmctl(shm_id, IPC_RMID, NULL);
	semctl(sem_id,0,IPC_RMID,0);
	
	return 0;
}

void sem_Lock (int sem_id){
    buffer.sem_num=0;
    buffer.sem_flg=0;
    buffer.sem_op=-1;
    if(semop(sem_id,&buffer,1)==-1)
        printf("Errore blocco semaforo\n");
}

void sem_Unlock (int sem_id){
    buffer.sem_num=0;
    buffer.sem_flg=0;
    buffer.sem_op=1;
    if(semop(sem_id, &buffer, 1)==-1)
        printf("Errore sblocco semaforo\n");
}
