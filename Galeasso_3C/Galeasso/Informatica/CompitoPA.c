/*
Galeasso Federico 3C
Data base e altezza, calcolare il perimetro e l'area del rettangolo.
*/

#include <stdio.h>
int main (){
	int Base, Altezza, Perimetro, Area;
	printf("Inserisci la base: \n");
	scanf("%d", &Base);
	printf("Inserisci l'altezza: \n");
	scanf("%d", &Altezza);
	Perimetro=(Base+Altezza)*2;
	Area=Base*Altezza;
	printf("Calcolo del PERIMETRO: il risultato di (%d+%d)*2 è %d\n", Base, Altezza, Perimetro);
	printf("Calcolo dell'AREA: il risultato di %d*%d è %d\n", Base, Altezza, Area);
return 0;
}
