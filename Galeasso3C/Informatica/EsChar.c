// Galeasso Federico 3C 24/11/2021 Primo esercizio CHAR

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {

	char c; //CHAR
	
	for(c='A'; c<='z'; c++){ // stampa dalla A alla Z, caratteri,  e poi dalla a alla z
	
		if(c<='Z' || c>='a'){ // con questo if stampa dalla A alla z e e dalla a alla z senza caratteri
		
			printf("%c ", c);
		}
		
	}
	
	printf("\n");
	
return 0;
}
