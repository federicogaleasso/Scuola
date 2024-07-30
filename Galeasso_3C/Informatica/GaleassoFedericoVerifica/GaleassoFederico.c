//Galeasso Federico 3C 16/11/21 VERIFICA
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int Npersone=0, Menu=0, i=1, Bevande=0, Consegna=0, Totale=0;
	srand(time(NULL));
	Npersone=rand()%21+5; //(25-5+1)+5
	printf("Le persone sono %d\n", Npersone);
	printf("Scegliere i menù\n1(3pz, 8€)\n2(6pz, 14€)\n3(da 6 a 10pz, 25€)\n4(oltre 10pz, 32€).\n");
	for(i=1; i<Npersone; i++){
		printf("Persona %d: ", i);
		scanf("%d", &Menu);
		switch(Menu){
			case 1:
				Menu=8;
				printf("Inserisci 1 per bevanda, 0 per no.\n");
				scanf("%d", &Bevande);
					if(Bevande==1){
					Bevande=rand()%9+2; //(10-2+1)+2
					printf("Hai %d bevande\n", Bevande);
					Bevande=2*Bevande;
					printf("%d\n", Bevande);
					}
					printf("Vuoi la consegna a domicilio? 1 si, 0 no.\n");
					scanf("%d", &Consegna);
					if(Consegna==1){
					printf("Hai la consegna a domicilio.\n");
					Menu=Menu+5;
					printf("%d\n", Menu);
					}
				break;
			case 2:
				Menu=14;
				printf("Inserisci 1 per bevanda, 0 per no.\n");
				scanf("%d", &Bevande);
					if(Bevande==1){
						Bevande=rand()%9+2; //(10-2+1)+2
						printf("Hai %d bevande\n", Bevande);
						Bevande=2*Bevande;
						printf("%d\n", Bevande);
						}
					printf("Vuoi la consegna a domicilio? 1 si, 0 no.\n");
					scanf("%d", &Consegna);
					if(Consegna==1){
					printf("Hai la consegna a domicilio.\n");
					Menu=Menu+5;
					printf("%d\n", Menu);
					}
				break;
			case 3:
				Menu=25;
				printf("Inserisci 1 per bevanda, 0 per no.\n");
				scanf("%d", &Bevande);
					if(Bevande==1){
						Bevande=rand()%9+2; //(10-2+1)+2
						printf("Hai %d bevande\n", Bevande);
						Bevande=2*Bevande;
						printf("%d\n", Bevande);
						}
					printf("Vuoi la consegna a domicilio? 1 si, 0 no.\n");
					scanf("%d", &Consegna);
					if(Consegna==1){
					printf("Hai la consegna a domicilio.\n");
					Menu=Menu+5;
					printf("%d\n", Menu);
					}
				break;
			case 4:
				Menu=32;
				printf("Inserisci 1 per bevanda, 0 per no.\n");
				scanf("%d", &Bevande);
					if(Bevande==1){
						Bevande=rand()%9+2; //(10-2+1)+2
						printf("Hai %d bevande\n", Bevande);
						Bevande=2*Bevande;
						printf("%d\n", Bevande);
						}
					printf("Vuoi la consegna a domicilio? 1 si, 0 no.\n");
					scanf("%d", &Consegna);
					if(Consegna==1){
					printf("Hai la consegna a domicilio.\n");
					Menu=Menu+5;
					printf("%d\n", Menu);
					}
				break;
			default:
			printf("Hai scelto un menù non valido!\n");
		}
	}
	/*Totale=Menu;
	printf("%d", Totale);
	*/
return 0;
}
