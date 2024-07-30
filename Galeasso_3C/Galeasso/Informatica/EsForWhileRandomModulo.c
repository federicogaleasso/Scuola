/*
Galeasso Federico 3C 9/11/2021
Estrarre casualmente 20 numeri pari compresi tra 50 e 150, stamparli e dire quanti di questi sono multipli di 3
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int Valore=0, i=0;
	srand(time(NULL));
	//(Massimo-Minimo+1)+Minimo
	for(i=0;i<20;i++){
		Valore=rand()%101 + 50;
		printf("%d\n", Valore);
	}
	//while(){
	
	//}
return 0;
}
