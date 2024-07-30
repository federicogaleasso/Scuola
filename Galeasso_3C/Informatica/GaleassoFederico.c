/*
Galeasso Federico 3C 5/10/2021
Verifica
*/
#include <stdio.h>
int main(){
	int N, M, Saloperai, Salimpiegati, Incentivo, TotsalN, TotsalM, DifferenzatotNM, Tottutti, Totsalannui, Anno;
	float Stipmedio;
	Saloperai=1050;
	Salimpiegati=1325;
	Incentivo=80;
	Anno=12;
	printf("\n*****DITTA di MANUFATTI*****\n");
	printf("\n-Calcolo degli stipendi dei lavoratori-\n");
	printf("\n* * * * * * * * * * * * * * * * * * * *\n");
	printf("\nInserisci il numero degli operai:\n");
	scanf("%d", &N);
	printf("Inserisci il numero degli impiegati:\n");
	scanf("%d", &M);
	printf("\n************************************\n");
	TotsalN=(Saloperai+Incentivo)*N;
	TotsalM=(Salimpiegati+Incentivo)*M;
	DifferenzatotNM=TotsalN-TotsalM;
	Tottutti=TotsalN+TotsalM;
	Stipmedio=(float)Tottutti/(N+M);
	Totsalannui=(TotsalN*Anno)+(TotsalM*Anno);
	printf("\nIl salario mensile degli operai è di %d€\n", TotsalN);
	printf("Il salario mensile degli impiegati è di %d€\n", TotsalM);
	printf("La differenza tra il totale del salario degli operai e il totale del salario degli impiegati è di %d€\n", DifferenzatotNM);
	printf("Il totale dei salari mensili di tutti i lavoratori è di %d€\n", Tottutti);
	printf("Lo stipendio medio mensile di tutti i lavoratori è di %.2f€\n", Stipmedio);
	printf("Il totale dei salari annui di tutti i lavoratori è di %d€\n\n", Totsalannui);
return 0;
}

