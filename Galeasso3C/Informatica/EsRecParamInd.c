// Galeasso Federico 3C 1/2/2022 Esercizio di Recupero in preparazione alla verifica
// Dati N numeri cerare una funzione che conti i pari, in dispari e la media e li restituisca al main.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int creaNumero(int, int);
void conta(int, int *, int *, float *);

int main(){
	int numero, contap=0, contad=0;
	float media=0.0;
	srand(time(NULL));
	numero=creaNumero(15,5);
	printf("Creo %d numeri\n", numero);
	printf("Valore dei pari --> %d\nValore dei dispari --> %d\n", contap, contad);
	conta(numero, &contap, &contad, &media);
	printf("Valore dei pari --> %d\nValore dei dispari --> %d\n", contap, contad);
	printf("La media dei numeri è %.2f\n", media);
return 0;
}

int creaNumero(int max, int min){
	int num;
	num=rand()%(max-min+1)+min;
return num;
}

void conta(int n, int *cp, int *cd, float *m){
	int i, num, somma=0;
	for(i=0; i<n; i++){
		num=creaNumero(100,60);
		somma=somma+num;
		printf("Numero creato --> %d\n", num);
		if(num%2==0){
			*cp=*cp+1; //(*cp)++;
		}else{
			*cd=*cd+1;
		}
	}
	*m=(float)somma/n;
}
