// Galeasso Federico 3C 11/5/2022	|	PRIMO PROGRAMMA IN ASSEMBLY (Hello World!)

// Per COMPILARE il file --> gcc HelloWorldAssembly.s -o HelloWorldAssembly -m32

// PACCHETTI DA INSTALLARE:
// sudo apt-get install gcc-multilib
// sudo apt-get install ddd

//Per commenti sulla stessa riga del codice usare il #

.data		#qui si inseriscono le variabili globali e le costanti

hello:	.string	"Hello World!\n"
	
.text		#qui dentro c'è tutto il codice

	.global	main		#fa riferimento all'etichetta MAIN
	
main:		#etichetta MAIN
		
		movl		$4, %eax		#la MOV vuole --> SORGENTE, DESTINAZIONE		#write --> printf in c
		movl		$1, %ebx
		movl		$hello, %ecx
		movl		$13, %edx
		int		$0x80
		
			//RETURN
			
		movl		$1, %eax
		movl		$0, %ebx
		int		$0x80
