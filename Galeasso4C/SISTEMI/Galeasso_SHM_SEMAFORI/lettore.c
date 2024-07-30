//GALEASSO FEDERICO 4C 28/11/2022 COMPITO SHM-SEMAFORI - FILE LETTORE

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
	
	shmid=shmget(keyshm, SHM_SIZE, 0666);	//3 PARAMETRI: 1) CHIAVE MEMORIA , 2) DIMENSIONE MEMORIA , 3) PERMESSI
	
	semid=semget(keysem, 1, 0666 | IPC_EXCL); //3 PARAMETRI: 1) CHIAVE SEMAFORO , 2) NUMERO DI SEMAFORI DA CREARE , 3)FLAG PERMESSI E UTILIZZO ESCLUSIVO
	
	if((shmid==-1) || (semid==-1)){	//CONTROLLO DI ERRORE
		printf("Errore nella creazione della memoria o del semaforo\n");
		exit(-1);
	}
	
	//NEL LETTORE NON SI SETTA DEL SEMAFORO
	
	 
	dati=(char *)shmat(shmid, NULL, SHM_RDONLY);	//CI AGGANCIAMO ALL'AREA DI MEMORIA
	
	//controllare i valori di ritorno di dati
	
	//ora controlliamo se il semaforo è LIBERO. Se è libero BLOCCHIAMO il semaforo e facciamo tutte le operazioni sulla MEMORIA. Dopo che abbiamo finito, SBLOCCHIAMO il SEMAFORO
	
	while(strcmp(dati,"fine")!=0){
		if(semctl(semid, 0, GETVAL)==1){
			semLock(semid);	//FUNZIONE CHE BLOCCA IL SEMAFORO
			printf("%s\n",dati);
			semUnlock(semid);	//FUNZIONE CHE SBLOCCA IL SEMAFORO
		}
	}
	
	//IL LETTORE NON DISTRUGGE LA MEMORIA
	
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
