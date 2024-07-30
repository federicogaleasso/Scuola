/*
Galeasso Federico
Compito
Chiedere all'utente quanti numeri vuole inserire e memorizzare tale valore in N.
Ripetere N volte la richiesta di un numero float all'utente.
Chiudere il programma con la stampa della media degli N numeri float inseriti.

Es.

Inserisci quanti numeri vuoi elaborare: 3

Inserisci il 1° numero: 6.5
Inserisci il 2° numero: 2.5
Inserisci il 3° numero: 3

La media dei numeri immessi è 4.00
*/

#include <stdio.h>

int main(){
    
    int N=0, i=1;
    float media=0, somma=0.00, num=0.00;
    
    printf("\nQuanti numeri vuoi inserire? ");
    scanf("%d", &N);
    
    while(i <= N){
         
         printf("Inserisci il %d° numero: ", i);
         scanf("%f", &num);
         
         somma=somma+num;
         
         i++;
         num=0.00;
    }
    
    media=somma/N;
    
    printf("La media dei %d numeri è %.2f \n\n", N, media);

    return 0;
}

