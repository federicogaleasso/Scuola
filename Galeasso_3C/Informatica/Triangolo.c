/*
Federico Galeasso 3C 3/11/2021
Stabilire se dati i 3 dati di un triangolo, esso può essere in effetti un triangolo e se è equilatero, scaleno, isoscele e/o rettangolo.
E' un triangolo se ogni lato è più piccolo della somma degli altri due.
*/
#include <stdio.h>
int main (){
	int L1=0, L2=0, L3=0, Somma1=0, Somma2=0, Somma3=0;
	printf("Inserisci il primo lato: ");
	scanf("%d", &L1);
	printf("Inserisci il secondo lato: ");
	scanf("%d", &L2);
	printf("Inserisci il terzo lato: ");
	scanf("%d", &L3);
	if(L1 < (L2+L3) && L2 < (L1+L3) && L3 < (L1+L2)){
		if(L1 == L2 && L2 == L3 && L3 == L2){
			printf("E' un triangolo equilatero\n");
		}
		if(L1 != L2 && L2 != L3 && L3 != L1){
			printf("E' un triangolo scaleno\n");
		}
		if(L1 == L2 && L3 != L1 && L2 || L2 == L3 && L1 != L2 && L3 || L3 == L1 && L2 != L3 && L1){
			printf("E' un triangolo isoscele\n");
		}
	}
	else{
		printf("Non è un triangolo\n");
	}
return 0;
}
