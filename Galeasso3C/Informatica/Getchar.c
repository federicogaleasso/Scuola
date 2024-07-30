#include<stdio.h>
int main(){
	char Carattere=' ';
	printf("Inserisci un carattere: ");
	Carattere=getchar();
	while(getchar()!='\n');
	printf("%c", Carattere);

return 0;
}
