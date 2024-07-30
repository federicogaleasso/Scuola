/*
GALEASSO FEDERICO 4C 11/10/2022 IO SONO LEGGENDA

“Io sono leggenda”
Tutto ebbe inizio quando il padre, creò il “Grande File” chiamato  leggenda.txt  e vi scrisse questerighe:
“Narra la leggenda che un padre di nome  PID_PADRE  creò  N  figli, li affidò al loro destino edinsieme scrissero la Storia. Questa Storia racconta di leggende epiche, duri scontri, ardue battaglie,alcune sconfitte e molte vittorie”
Ognuno degli N figli creati aveva il compito, nella sua vita, di lottare contro incantesimi e malefici per   la   propria   sopravvivenza.   L’unica   maniera   per   sopravvivere   era   di   generare   casualmente   unnumero compreso tra 1977 e 1986 e divisibile per due. Chi riusciva nell’impresa, dopo il grido divittoria (da stampare a video) e prima di terminare la sua vita in modo dignitoso, aveva la possibilitàdi aggiungere la sua impresa al “Grande File”, con la seguente riga:
“Io PID, figlio di PID_padre, eroico cavaliere, dopo aver affrontato tremende battaglie, posso diredi aver vinto la mia guerra con il numero numero_generato” Il  padre,  dopo  una vita  di  sofferenze  per la  morte  di  tutti  i figli,  prima  di  morire,  volle  rendereomaggio anche ai figli caduti in battaglia, per tale motivo, decise di aggiungere al “Grande File” ilseguente messaggio:“Figli miei  PID_X, PID_Y, PID_Z, (...) avete lottato tutti con grande coraggio e mi avete resoorgoglioso di voi. Siete caduti, ma il vostro nome rimarrà per sempre inciso nella Storia."
NOTE:
•N è chiesto in input all’utente
•Tutti i figli devono terminare in modo corretto
•PID_X, PID_Y, PID_Z (...) è l’elenco dei PID dei figli deceduti in battaglia.
Suggerimenti per la gestione del file:
FILE *fp;
fp=fopen(“nomeFile”, “a”);
fprintf(fp, testo_da_scrivere);
fclose(fp);
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	system("clear");

	pid_t ChiSono, pid;
	int figli, i, numero, stato_wait, min=1977, max=1986;

	printf("Quanti figli vuoi generare? --> ");
	scanf("%d", &figli);
	
	//APERTURA DEL FILE
	FILE * fp;
	fp = fopen("/home/docente/Scrivania/Galeasso_IoSonoLeggenda/leggenda.txt", "w");
		  
	//SCRITTURA DEL FILE
	fprintf(fp, "Narra la leggenda che un padre di nome  %d  creò %d figli, li affidò al loro destino ed insieme scrissero la Storia. Questa Storia racconta di leggende epiche, duri scontri, ardue battaglie,alcune sconfitte e molte vittorie\n", getpid(), figli);   
	fclose(fp);

	//INIZIO codice di TUTTI i FIGLI
	for(i=0; i<figli; i++){
		if((ChiSono=fork())<0){
			printf("Errore durante la creazione della fork()\nChiusura programma in corso...\n");
			exit(-1);
		}
		
		if(ChiSono==0){
			srand(getpid());
			numero=rand()%(max-min+1)+min;
			printf("Figlio: %d | Numero: %d\n", getpid(), numero);
			if(numero%2==0){
				printf("Sono il figlio %d e ho vinto!\n", getpid());
				//APERTURA DEL FILE
				FILE * fp;
				fp = fopen("/home/docente/Scrivania/Galeasso_IoSonoLeggenda/leggenda.txt", "a");

				//SCRITTURA DEL FILE
				fprintf(fp, "Io %d, figlio di %d, eroico cavaliere, dopo aver affrontato tremende battaglie, posso dire di aver vinto la mia guerra con il numero %d\n", getpid(), getppid(), numero);   
				fclose(fp);
			}
			
			if(numero%2!=0){
				printf("Sono il figlio %d e ho perso...\n", getpid());
				//APERTURA DEL FILE
				FILE * fp;
				fp = fopen("/home/docente/Scrivania/Galeasso_IoSonoLeggenda/leggenda.txt", "a");

				//SCRITTURA DEL FILE
				fprintf(fp, "Figli miei, avete lottato tutti con grande coraggio e mi avete reso orgoglioso di voi. Siete caduti, ma il vostro nome rimarrà per sempre inciso nella Storia.\n");   
				fclose(fp);
			}
			exit(numero);
		}
	}
	//FINE codice di TUTTI i FIGLI

	//INIZIO codice processo PADRE
	for(i=0; i<figli; i++){	
		pid=wait(&stato_wait);
		stato_wait=stato_wait/256;
	}
	//FINE codice processo PADRE

return 0;
}
