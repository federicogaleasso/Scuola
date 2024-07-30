//SCRITTORE

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>
#include <sys/wait.h>

#define SHM_SIZE 1024
struct sembuf buffer;

void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);


int main(){
	system("clear");
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, i, flag1=0, tavolo, commensali, *dati, fine=0, pid, pidstato, status, cont0=0, cont1=0, cont2=0;
	
	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666);
	sem_id = semget(sem_chiave, 1, 0666);         
  
	if (shm_id == -1 || sem_id == -1){
		printf("Errore nella gestione della memoria o dei semafori\n");
		exit(-1);
	}
	
	dati=(int *) shmat(shm_id, NULL,0);
	
	printf("Inserisci il numero di commensali (tra 20 e 50): ");
	scanf("%d",&commensali);
	while(commensali<20 || commensali>50){
		printf("ERRORE! Inserisci il numero di commensali (tra 20 e 50): ");
		scanf("%d",&commensali);
	}
	
	for(i=1;i<=(commensali*2);i=i+2){
		if((pid=fork())<0){
			printf("Errore creazione fork()\n");
			exit(-2);
		}
		if(pid==0){
	        srand(getpid());
	        tavolo=rand()%3;
	        while(flag1==0){
				if(semctl(sem_id, 0, GETVAL)==1){
					sem_Lock(sem_id);
					dati[i]=getpid();
					dati[i+1]=tavolo;
					if(tavolo==0){
						printf("Commensale: %d | Tavolo: %d (menu a base di pesce)\n ", getpid(), tavolo);
						cont0++;
						//printf("%d\n", cont0);
						if(cont0==4){
							printf("Tavolo 0 pieno!\n");
						}
					}
					if(tavolo==1){
						printf("Commensale: %d | Tavolo: %d (menu a base di carne)\n ", getpid(), tavolo);
						cont1++;
						//printf("%d\n", cont1);
						if(cont1==4){
							printf("Tavolo 1 pieno!\n");
						}
					}
					if(tavolo==2){
						printf("Commensale: %d | Tavolo: %d (menu vegetariano)\n ", getpid(), tavolo);
						cont2++;
						//printf("%d\n", cont2);
						if(cont2==4){
							printf("Tavolo 2 pieno!\n");
						}
					}
					flag1=1;
					sem_Unlock(sem_id);
					exit(tavolo);
				}
	        }
	    }
	}
	
	for(i=0;i<commensali;i++){
	   pidstato=wait(&status);
	}
	
	printf("%d commensali hanno scelto il tavolo 0\n%d commensali hanno scelto il tavolo 1\n%d commensali hanno scelto il tavolo 2\n", cont0, cont1, cont2);
	
	printf("Tutti i commensali hanno hanno mangiato\n");
	
	while(fine!=1){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			dati[0]=commensali;
			fine=1;
			sem_Unlock(sem_id);
		}
	}
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
