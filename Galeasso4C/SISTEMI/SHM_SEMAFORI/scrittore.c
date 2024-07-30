//GALEASSO FEDERICO 4C 22/11/2022 APPUNTI SUI SEMAFORI - FILE SCRITTORE

//INCLUSIONE LIBRERIE --> NUOVA LIBRERIA: #include <sys/sem.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

#define SHM_SIZE 1024	//DIMENSIONE MEMORIA
struct sembuf buffer; //STRUTTURA DI TIPO sembuf

void semLock(int);
void semUnlock(int);

int main(){
	key_t keyshm=1234, keysem=5678; //keyshm --> chiave memoria , keysem --> chiave semaforo
	int shmid, semid, sem_stato;	//shmid --> id memoria , semid --> id semaforo , sem_stato --> verifichiamo se è andato a buon fine o no
	char *dati, stringa[20];
	
	shmid=shmget(keyshm, SHM_SIZE, 0666 | IPC_CREAT);	//3 PARAMETRI: 1) CHIAVE MEMORIA , 2) DIMENSIONE MEMORIA , 3)FLAG PERMESSI E CREAZIONE
	
	semid=semget(keysem, 1, 0666 | IPC_CREAT); //3 PARAMETRI: 1) CHIAVE SEMAFORO , 2) NUMERO DI SEMAFORI DA CREARE , 3)FLAG PERMESSI E CREAZIONE
	
	if((shmid==-1) || (semid==-1)){	//CONTROLLO DI ERRORE
		printf("Errore nella creazione della memoria o del semaforo\n");
		exit(-1);
	}
	
	//SETTO DEL SEMAFORO
	sem_stato=semctl(semid, 0, SETVAL, 1);	//RESTITUISCE UN INTERO. 4 PARAMETRI: 1) ID SEMAFORO , 2) IDENTIFICHIAMO LA PRIMA CELLA DEL VETTORE , 3) COMANDO --> SETVAL --> setta il valore iniziale del semaforo (in questo caso --> 1)
	
	 
	dati=(char *)shmat(shmid, NULL, 0);	//CI AGGANCIAMO ALL'AREA DI MEMORIA
	
	//controllare i valori di ritorno di dati e sem_stato
	
	//ora controlliamo se il semaforo è LIBERO. Se è libero BLOCCHIAMO il semaforo e facciamo tutte le operazioni sulla MEMORIA. Dopo che abbiamo finito, SBLOCCHIAMO il SEMAFORO
	
	while(1){
		if(semctl(semid, 0, GETVAL)==1){
			semLock(semid);	//FUNZIONE CHE BLOCCA IL SEMAFORO
			printf("Inserisci una stringa: ");
			scanf("%s", stringa);
			strcpy(dati, stringa);
			semUnlock(semid);	//FUNZIONE CHE SBLOCCA IL SEMAFORO
		}
	}
	
	//DISTRUZIONE MEMORIA
	sem_stato=semctl(semid, 0, IPC_RMID, 0);
	shmctl(shmid, IPC_RMID, NULL);
	
return 0;
}

//FUNZIONE CHE BLOCCA IL SEMAFORO
void semLock(int id){
	buffer.sem_num=0; 	//INDICE DEL SEMAFORO SU CUI VOGLIAMO OPERARE
	
	buffer.sem_flg=0;	//FLAG DI SCRITTURA --> O
	
	buffer.sem_op=-1;	//È L'OPERAZIONE DI DECREMENTO
	
	if(semop(id, &buffer, 1)==-1){
		printf("Errore blocco semaforo\n");
	} else{
		printf("Operazione riuscita! Semaforo bloccato\n");
	}
}

//FUNZIONE CHE SBLOCCA IL SEMAFORO
void semUnlock(int id){
	buffer.sem_num=0; 	//INDICE DEL SEMAFORO SU CUI VOGLIAMO OPERARE
	
	buffer.sem_flg=0;	//FLAG DI SCRITTURA --> O
	
	buffer.sem_op=1; //È L'OPERAZIONE DI DECREMENTO
	
	if(semop(id, &buffer, 1)==-1){
		printf("Errore blocco semaforo\n");
	} else{
		printf("Operazione riuscita! Semaforo bloccato\n");
	}
}
