/*
Galeasso Federico 3C 27/11/2021
Creare un programma che permetta di mostrare all'utente il seguente menu (finchè l'utente non preme E per uscire):
A. data una lettera, stampare la successiva
B. data una lettera minuscola, convertirla in maiuscolo
C. data una lettera stabilire se è una vocale oppure una consonante
D. dati 8 numeri, contare i positivi
E. Esci
*/
#include<stdio.h>
int main(){
	int i=0, N=0, Contatore=0, Piu=1;
	char	Menu=' ', Lettera=' ', Invio;
	printf("Scegli una delle seguenti opzioni:\nA. data una lettera, stampare la successiva\nB. data una lettera minuscola, convertirla in maiuscolo\nC. data una lettera stabilire se è una vocale oppure una consonante\nD. dati 8 numeri, contare i positivi\nE. Esci\n\n");
	Menu=getchar();
	Invio=getchar();
	switch(Menu){
		case 'A':
		case 'a':
			printf("Inserisci una lettera: ");
			scanf("%c", &Lettera);
			if(Lettera=='Z' || Lettera=='z'){
			printf("E' l'ultima lettera dell'alfabeto!\n");
			}
			else{
			printf("La lettera successiva alla lettera %c è la lettera %c\n", Lettera, Lettera+1);
			}
		break;
		case 'B':
		case 'b':
			printf("Inserisci una lettera: ");
			scanf("%c", &Lettera);
			if(Lettera=='a' || Lettera=='b' || Lettera=='c' || Lettera=='d' || Lettera=='e' || Lettera=='f' || Lettera=='g' || Lettera=='h' || Lettera=='i' || Lettera=='j' || Lettera=='k' || Lettera=='l' || Lettera=='m' || Lettera=='n' || Lettera=='o' || Lettera=='p' || Lettera=='q' || Lettera=='r' || Lettera=='s' || Lettera=='t' || Lettera=='u' || Lettera=='v' || Lettera=='w' || Lettera=='x' || Lettera=='y' || Lettera=='z'){
			printf("Lettera %c in MAIUSCOLO --> %c\n", Lettera, Lettera-32);
			}
			else{
			printf("La lettera %c è già MAIUSCOLA!\n", Lettera);
			}
		break;
		case 'C':
		case 'c':
			printf("Inserisci una lettera: ");
			scanf("%c", &Lettera);
			if(Lettera=='A' || Lettera=='E' || Lettera=='I' || Lettera=='O' || Lettera=='U' || Lettera=='a' || Lettera=='e' || Lettera=='i' || Lettera=='o' || Lettera=='u'){
				printf("La lettera %c è una VOCALE.\n", Lettera);
			}
			else{
				printf("La lettera %c è una CONSONANTE.\n", Lettera);
			}
		break;
		case 'D':
		case 'd':
			printf("Inserisci 8 numeri\n ");
			for(i=0; i<8; i++){
			printf("Inserisci il %d° numero: ", Piu);
			scanf("%d", &N);
			Piu++;
				if(N>=0){
					Contatore++;
				}
			}
			printf("I numeri positivi sono %d.\n", Contatore);
		break;
		case 'E':
		case 'e':
			printf("Programma terminato!\n");
		break;
		default:
		printf("Hai inserito una lettera non valida!\n");
	}
return 0;
}
