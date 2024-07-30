//GALEASSO FEDERICO 4C 4/10/2022 VERIFICA ARSENIO LUPIN

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int i=0, numero, stato_wait, min=1, max=6, bottino=0, numeroLup=0, somma=0, continuare=0, esci=0;
	
	printf("\e[1;93m*****\e[0m\e[1;94mBENVENUTO\e[0m\e[1;93m*****\e[0m\n\n");
	
	printf("\e[1;97mInserisci il valore iniziale del \e[1;96mbottino\e[0m\e[1;97m --> \e[1;96m");
	scanf("%d", &bottino);
	
	while(esci==0){
	
		printf("\e[0m\e[1;94m\n-ROUND %d-\n\e[0m", i=i+1);
	
		if((ChiSono=fork())<0){
			printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
			exit(-1);
		}
		
		if(ChiSono==0){
			printf("\e[0m\e[1;97mInserisci il numero dell'\e[1;93mISPETTORE \e[1;97m--> \e[1;93m");
			scanf("%d", &numero);
			//printf("Ispettore: %d | Numero: %d\n\n", getpid(), numero);
			exit(numero);
		}
	
		//
		
		pid=wait(&stato_wait);
		stato_wait=(stato_wait/256);
		srand(time(NULL));
		numeroLup=rand()%(max-min+1)+min;
		printf("\e[0m\e[1;97mNumero di \e[1;95mLUPIN \e[1;97m--> \e[1;95m%d\n", numeroLup);
		somma=stato_wait+numeroLup;
		if(somma%2==0){
			printf("\n\e[0m\e[1;97mLa somma dei numeri è \e[1;92mPARI\e[1;97m --> Vince l'\e[1;93mISPETTORE\e[0m\n");
			bottino=bottino-20;
		} else{
			printf("\n\e[0m\e[1;97mLa somma dei numeri è \e[1;91mDISPARI\e[1;97m --> Vince \e[1;95mLUPIN\e[0m\n");
			bottino=bottino+10;
		}
		
		printf("\n\e[1;97mVuoi giocare ancora (\e[1;94m1\e[1;97m per continuare | \e[1;94m0\e[1;97m per uscire)? --> \e[1;94m");
		scanf("%d", &continuare);
		if(continuare==0 || bottino<=0){
			printf("\n\e[0m\e[1;96mBottino finale \e[1;97m--> \e[1;96m%d\n", bottino);
			esci=1;
		}
	}

return 0;
}
