/*
Galeasso Federico 3C 26/5/2022 | Es. vettori stringhe - Gruppi universitari

Un gruppo di N studenti universitari (N compreso tra 2 e 20), si iscrive ad un esame, inserendo in input il proprio cognome. Di questi N studenti si vogliono formare due gruppi:
il primo gruppo contenente tutti gli studenti con l'iniziale del cognome compresa tra A ed L
Il secondo gruppo contenente tutti gli studenti con l'iniziale del cognome compresa tra M e Z
Visualizzare a video:
- L'elenco completo di tutti gli studenti iscritti
- L'elenco degli studenti appartenenti al primo gruppo
- L'elenco degli studenti appartenenti al secondo gruppo
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MIN 2
#define NOMI 20
#define CAR 80

//PROTOTIPI
void carica(char[][CAR]);

int main(){
	char studenti[NOMI][CAR];
	system("clear");
	
	carica(studenti);
return 0;
}

void carica(char studenti[][CAR]){
    int n, i, p=1;
    char vett[CAR];
    
    printf("Quanti studenti vuoi inserire? ");
    scanf("%d", &n);
    
    while(n<MIN || n>NOMI){
     printf("\tERRORE! Il numero deve essere compreso tra %d e %d, reinserisci: ", MIN, NOMI);
     scanf("%d", &n);
    }
    
    while(getchar()!='\n');
    for(i=0;i<n;i++){
		printf("Inserisci in nome del %d° studente: ", p++);
		gets(vett);     
    }
    printf("\n");
}
