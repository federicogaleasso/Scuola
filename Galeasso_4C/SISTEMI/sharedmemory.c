//GALEASSO FEDERICO 4C 24/10/2022 PRIMO ESERCIZIO SULLA MEMORIA CONDIVISA

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

#define SHM_SIZE 1024	//costante --> dimensione della memoria

int main(){
	key_t chiave=1234; //è la chiave della memoria (è come una password) inventata da noi. ATTENZIONE!!! LA CHIAVE 0000 DA PROBLEMI!!!
	int shmid; //id memoria
	
	pid_t chiSono;

	//CREAZIONE DELLA MEMORIA
	shmid=shmget(chiave, SHM_SIZE , 0666 | IPC_CREAT)	//parametro 3 --> 0666 numero in ottale, da i permessi di lettura e scrittura e IPC_CREAT lo crea crea
	
	if(shmid==-1){
		printf("Errore nella creazione della memoria condivisa (shm)\n");
		exit(-1)
	}
	
	//UTILIZZO DELLA MEMORIA
	
	//FORK 1
	if((chiSono)=fork()<0){
		printf("Errore nella fork()\n");
		exit(-2)
	}
	
	if(chiSono==0){	//sono nel figlio scrittore
		scrittore(shmid);
		exit(0)
	} else{	//sono nel figlio padre. il padre aspetta solo il figlio
		wait(NULL)
	}
	
	//FORK 2
	if((chiSono)=fork()<0){
		printf("Errore nella fork()\n");
		exit(-2)
	}
	
	if(chiSono==0){	//sono nel figlio scrittore
		lettore(shmid);
		exit(0)
	} else{	//sono nel figlio padre. il padre aspetta solo il figlio
		wait(NULL)
	}
	
	//DISTRUZIONE DELLA MEMORIA
	shmctl(shmid, IPC_RMID , NULL)
	
return 0;
}
