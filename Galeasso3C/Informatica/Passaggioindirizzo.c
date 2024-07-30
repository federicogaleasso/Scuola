#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void scambia(int, int);

int main(){
	int N1, N2;
	srand(time(NULL));
	N1=rand()%10+1;
	printf("Numero 1 --> %d\n", N1);
	N2=rand()%20+1;
	printf("Numero 2 --> %d\n", N2);
	scambia(N1, N2);
	printf("N1 --> %d\n", N1);
	printf("N2 --> %d\n", N2);
return 0;
}

void scambia(int a, int b){
	int temp=0;
	temp=a;
	a=b;
	b=temp;
	printf("Dentro alla funzione\n");
	printf("a --> %d\n", a);
	printf("b --> %d\n", b);
}
