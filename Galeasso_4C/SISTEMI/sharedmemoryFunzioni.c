//GALEASSO FEDERICO 4C 8/11/2022 PRIMO ESERCIZIO SULLA MEMORIA CONDIVISA + FUNZIONE SCRITTORE E LETTORE

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

#define SHM_SIZE 1024	//costante --> dimensione della memoria

void scrittore(int);
void lettore(int);

int main(){
	key_t chiave=1234; //è la chiave della memoria (è come una password) inventata da noi. ATTENZIONE!!! LA CHIAVE 0000 DA PROBLEMI!!!
	int shmid; //id memoria
	
	pid_t chiSono;

	//CREAZIONE DELLA MEMORIA
	shmid=shmget(chiave, SHM_SIZE , 0666 | IPC_CREAT);	//parametro 3 --> 0666 numero in ottale, da i permessi di lettura e scrittura e IPC_CREAT lo crea crea
	
	if(shmid==-1){
		printf("Errore nella creazione della memoria condivisa (shm)\n");
		exit(-1);
	}
	
	//UTILIZZO DELLA MEMORIA
	
	//FORK 1
	if((chiSono=fork())<0){
		printf("Errore nella fork()\n");
		exit(-2);
	}
	
	if(chiSono==0){	//sono nel figlio scrittore
		scrittore(shmid);
		exit(0);
	} else{	//sono nel figlio padre. il padre aspetta solo il figlio
		wait(NULL);
	}
	
	//FORK 2
	if((chiSono=fork())<0){
		printf("Errore nella fork()\n");
		exit(-2);
	}
	
	if(chiSono==0){	//sono nel figlio lettore
		lettore(shmid);
		exit(0);
	} else{	//sono nel figlio padre. il padre aspetta solo il figlio
		wait(NULL);
	}
	
	//DISTRUZIONE DELLA MEMORIA
	shmctl(shmid, IPC_RMID , NULL);
	
return 0;
}

//PROCEDURA SCRITTORE
void scrittore(int id){
	int *p;	//puntatore
	int i,num;
	p=(int *)shmat(id,NULL,0);	//casting in intero. shmat --> id, NULL, shmflg (0: lettura e scrittura). Ci siamo agganciati alla memoria
	if(p==(int *)-1){
		("Errore nella shmat()\n");
		exit(-1);
	}
	for(i=0;i<5;i++){
		printf("Inserisci un numero: ");
		scanf("%d",&num);
		p[i]=num;	//in questo modo salviamo il valore di num in p, cioè nella memoria condivisa
	}
}

//PROCEDURA LETTORE
void lettore(int id){
	int *p;	//puntatore
	int i;
	p=(int*)shmat(id,NULL,SHM_RDONLY);	//casting in intero. shmat --> id, NULL, SHM_RDONLY (solo lettura). Ci siamo agganciati alla memoria
	if(p==(int *)-1){
		("Errore nella shmat()\n");
		exit(-3);
	}
	for(i=0;i<5;i++){
		printf("%d |",p[i]);	//in questo modo stampiamo i numeri
	}
	printf("\n");
}
