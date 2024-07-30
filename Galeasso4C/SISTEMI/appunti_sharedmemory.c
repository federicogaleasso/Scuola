//GALEASSO FEDERICO 4C 24/10/2022 APPUNTI SULLA MEMORIA CONDIVISA

//LIBRERIE PER I PROCESSI
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

//ECCO LE 3 FUNZIONI CHE USEREMO

//FUNZIONE 1
int shmget(key_t chiave, int dimensione, int shmflg) // la shmget permette di creare la memoria condivisa e vuole 3 parametri. Restituisce un intero (id) che sarà l'identificativo della memoria. PARAMETRI --> 1) chiave memoria, 2) dimensione memoria, 3) flag di creazione o di accesso

//FUNZIONE 2
void*shmat(int shmid, const void * shmaddr, int shmflg)	//restituisce un puntatore a void. per poter agganciarsi alla memoria gli serve: PARAMETRI --> 1) shmid (valore resituito da shmget), 2) è un puntatore alla struttura della memoria (lo mettiamo SEMPRE a NULL), 3) se shmlfg è --> lettura/scrittura | se è SHM_RDONLY --> solo lettura

//FUNZIONE 3
int shmctl(int shmid, int cmd, struct shmid_ds *buf)	//restituisce un intero. si mette alla fine e distrugge il segmento di memoria. 3 PARAMETRI --> 1) id memoria, 2)comando (intero). può essere SHM_LOCK/SHM_UNLOCK (blocca/sblocca il segmento) | IPC_SET/IPC_STAT (stato di memoria) | IPC_RMID (rimuove la memoria), 3) puntatore ad una struttura (lo settiamo SEMPRE a NULL)
