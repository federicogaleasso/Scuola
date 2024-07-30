/*
Compito Fattura Edile
Galeasso Federico 3C 9/10/2021
*/
#include <stdio.h>
int main(){
    int SCem=100, UNOSCem=5, SCemTOT=0, Trasporto=50;
	 float Totale=0, IvaTOT=0, Iva=0, TOTTutto=0, SGhiaiaPrezzo=0, CSicPrezzo=0, BVernPrezzo=0;
	 float Carriole=2, CarriolePrezzo=50, CarrioleTOT=0, CarrioleSconto=0, CarrioleFinale=0;
    SCemTOT=SCem*UNOSCem;
    CarrioleTOT=Carriole*CarriolePrezzo;
    CarrioleSconto=(5*CarrioleTOT)/100;
    CarrioleFinale=CarrioleTOT-CarrioleSconto;
    printf("\n*****FATTURA EDILE*****\n");
    printf("\nIl costo totale dei sacchi di cemento è di %d\n", SCemTOT);
    printf("Il costo totale delle cariole è di %.2f\n", CarrioleFinale);
    printf("\n----------------------------------\n");
    printf("\nInserisci il prezzo dei sacchi di ghiaia: \n€");
    scanf("%f", &SGhiaiaPrezzo);
    printf("Inserisci il prezzo dei caschi di sicurezza: \n€");
    scanf("%f", &CSicPrezzo);
    printf("Inserisci il prezzo dei barattoli di vernice: \n€");
    scanf("%f", &BVernPrezzo);
    printf("\n*********************************************\n");
    Totale=BVernPrezzo+CSicPrezzo+SGhiaiaPrezzo+CarrioleFinale+SCemTOT;
    Iva=(Totale*22)/100;
 	IvaTOT=Totale+Iva;
 	TOTTutto=IvaTOT+Trasporto;
    printf("\nIl costo totale con l'IVA e con i trasporti è di %.2f€\n\n", TOTTutto);
return 0;
}
