/*
Galeasso Federico 3C 21/12/2021 Esercizio Buffer Funzioni Parametrizzate

Data una frase fatta introdurre all'utente in input, scrivere un programma che, mediante le opportune funzioni e procedure parametrizzate, ne esamini i simboli e conti il numero di caratteri che rientrano nelle seguenti categorie:

* vocali

* consonanti

* cifre

* spazi

* "altri" caretteri
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void Char();

int main () {
	Char();
return 0;
}

void Char() {
	char L; 
	int N, Voc=0, i, Cons=0, Piu=1;
	printf("Numero di caratteri --> ");
	scanf("%d",&N);
	while(N<=0){
		printf("Numero di caratteri ( Inserisci un numero MAGGIORE di 0) --> ");
		scanf("%d",&N);
	}
	for(i=0; i<N; i++){
		while(getchar()!='\n');
		printf("%d° lettera --> ", Piu++);
		scanf("%c",&L);
		if (L=='A' || L=='E' || L=='I' || L=='O'|| L=='U' || L=='a'|| L=='e' || L=='i' || L=='o' || L=='u'){
			Voc++;
		} else if (L>='A'|| L>='a' || L<='Z' || L<='z' ){
			Cons++;
		}
	}
	printf("Cifre --> %d\n", N);
	printf("Vocali --> %d\n", Voc);
	printf("Consonanti --> %d\n",Cons);
}
