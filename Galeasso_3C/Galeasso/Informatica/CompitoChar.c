//Galeasso Federico 3C 24/11/2021 Compito CHAR
#include<stdio.h>
int main () {
	char c=' ';
	printf("Inserisci una lettera MINUSCOLA: ");
	scanf("%c", &c);
	while(c < 'a' || c > 'z'){
		printf("La lettera inserita è maiuscola. Reinserisci una lettara MINUSCOLA: ");
		scanf("%c", &c);
	}
	printf("Lettera %c in MAIUSCOLO --> %c\n ", c, c-32);
return 0;
}
