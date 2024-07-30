#include <stdio.h>
#include <stdlib>
#include <time.h>
int main(){
	int Stud=0, Somma=0, Voto, i;
	float Media=0.0;
	srand(time(NULL))
	while(Stud<1){
		printf("Quanti studenti? ");
		scanf("%d", &Stud);
	}
	for(i=0; i<Stud; i++){	//sintassi FOR //va da 0 a < di Stud (9), quindi dieci volte
		Voto=rand()%9+2 //va fino a  dieci //da 0 a 8, + 2 = 10
		//(max - min +1) + (min)
		//(10 - 2 + 1 = %9) + (2)
		printf("Voto: %d", Voto);
		Somma=Somma+Voto
	}
return 0;
}
