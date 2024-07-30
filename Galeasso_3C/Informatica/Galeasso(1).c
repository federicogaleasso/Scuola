//Galeasso Federico 3C 15/3/2022 Verifica

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 30

//Prototipi
int creaRandom(int, int);
void tipoCamera(char[]);
void giorniPerm(int[]);
void mediaG(int[]);
void totGD(int[]);
void stampaVet(char[], int[]);
void presenzeMax(int[]);
void cameraMaxRandom(int[]);

int main(){
	int camere[MAX], giorni[MAX];
	char tipologia[MAX];
	srand(time(NULL));
	tipoCamera(tipologia);
	giorniPerm(giorni);
	stampaVet(tipologia, giorni);
	mediaG(giorni);
	totGD(giorni);
	presenzeMax(giorni);
	cameraMaxRandom(giorni);
return 0;
}

int creaRandom(int min, int max){
return rand()%(max-min+1)+min;
}

void tipoCamera(char tipologia[]){
	int i=0;
	for(i=0; i<MAX; i++){
		while(tipologia[i] != 'S' && tipologia[i] != 'M' && tipologia[i] != 'T' && tipologia[i] != 'Q'){
			printf("Tipologia camera %d (S, M, T, Q): ", i+1);
			scanf("%c", &tipologia[i]);
			while(getchar()!='\n');
		}
	}
}

void giorniPerm(int giorni[]){
	int i=0;
	for(i=0; i<MAX; i++){
		giorni[i]=creaRandom(1,21);
		printf("Camera %d | %d\n", i+1, giorni[i]);
	}
}

void mediaG(int giorni[]){
	int i=0, somma=0;
	float media=0;
	for(i=0; i<MAX; i++){
		somma=somma+giorni[i];
	}
	media=(float)somma/MAX;
	printf("Media giorni: %.2f\n", media);
}

void totGD(int giorni[]){
	int i=0, somma=0;
	for (i=0; i<MAX; i++){
		if(giorni[i]%2 != 0){
			somma=somma+giorni[i];
		}
	}
	printf("Tot giorni disp: %d\n", somma);
}

void stampaVet(char tipologia[], int giorni[]){
	int i=0;
	for (i=0; i<MAX; i++){
		printf("Camera %d | Tipologia %c | Giorni %d\n", i+1, tipologia[i], giorni[i]);
	}
}

void presenzeMax(int giorni[]){
	int i=0, max=0;
	for(i=0; i<MAX; i=i+2){
		if(giorni[i]>max){
			max=giorni[i];
		}
	}
	printf("Max giorni: %d\n", max);
}

void cameraMaxRandom(int giorni[]){
	int i=0, num=0, massimo=0;
	num=creaRandom(1,21);
	printf("Numero random: %d\n", num);
	for(i=0; i<MAX; i++){
		if(giorni[i]>num){
			massimo=giorni[i];
			printf("Camera con %d giorni\n", massimo);
		}
	}
}
