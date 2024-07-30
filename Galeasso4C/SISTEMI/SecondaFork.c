//GALEASSO FEDERICO 4C 13/9/22 SECONDO ESERCIZIO PROCESSI
//Dato un numero, processo PADRE e FIGLIO lo modificano e lo stampano.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
	pid_t ChiSono;
	int numero=42;
	
	printf("Numero iniziale: %d\n", numero);
	
	if((ChiSono=fork())<0){
		printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
		exit(-1);
	}
	
	if(ChiSono==0){	//processo FIGLIO
		numero=8;
		printf("Sono il processo FIGLIO con PID %d, il numero modificato è %d\n", getpid(), numero);
	} else{	//processo PADRE
		numero=numero*5;
		printf("Sono il processo PADRE con PID %d, il numero modificato è %d\n", getpid(), numero);
	}
	
	printf("Numero alla fine del programma: %d\n", numero);
	
return 0;
}
