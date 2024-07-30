/*
Dato in input il prezzo di un prodotto, calcola e stampa il prezzo da pagare sapendo che se il prezzo è superiore a 3000€ applichi il 6% di sconto e, inoltre, se il pagamento avviene in contanti, devi applicare un ulteriore sconto del 2%.
*/
#include <stdio.h>
int main (){
	int Sconto1=6, Sconto2=2, Contanti=1, PrezzoDef=3000;
	float PrezzoP, Sconto, ScontoUlt;
	printf("Inserisci il prezzo del prodotto: ");
	scanf("%f", &PrezzoP);
	if(PrezzoP>PrezzoDef){
		Sconto=(PrezzoP*Sconto1)/100;
		printf("Il prezzo è di %.2f\n", Sconto);
		PrezzoP=PrezzoP-Sconto;
	}
	printf("Se paghi in contanti riceverai un ulteriore sconto del 2%%. Digita 1 se vuoi pagare in contanti.\n");
	scanf("%d", &Contanti);
	if(Contanti==1){
		ScontoUlt=(Sconto*Sconto2)/100;
		printf("Il prezzo è di %.2f\n", ScontoUlt);
	}
		else{
			if(Contanti!=1){
				printf("Non hai applicato lo sconto del 2%%\n");
			}
		}
	}
return 0;
}
