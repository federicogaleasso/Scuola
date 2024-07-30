/*
Galeasso Federico 3C 12/05/2022 Esercizio in classe STRINGHE

1) Chiedere ciclicamente 10 nomi di persone.
2) Memorizzarli nell'apposita struttura (vett di stringhe).
3) Stampare il vettore con i nomi in ordine di inserimento.
4) Ordinare alfabeticamente i nomi del vettore.
5) Ristampare il vettore
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

#define MAX 2000
#define LUN 2000

//PROTOTIPI


int main (){
	int number=0, i=0, s=1, I, J, FLAG, TMP;
	char testo[MAX][LUN], frase[LUN];
	system("clear");
	
	number = 0 ;
	for(i=0; i<10; i++){
		printf("Inserisci il %d nome: ", s);
		gets(frase) ;
		strcpy( testo[number], frase) ;
		number++ ;
		s++;
	}
	
	for(i=0; i<10; i++){
		puts(testo[i]);
	}
	
	/*
	J=N;
	FLAG=1;
	while(FLAG==1){
		FLAG=0;
		for(I=0; I<(J-1); I++){
			if(testo[I]>testo[I+1]){
				TMP=V[I];
				testo[I]=V[I+1];
				testo[I+1]=TMP;
				FLAG=1;
			}
		}
		J=J-1;
	}
	*/
	
return 0;
}
