// Galeasso Federico 3C 11/5/2022	|	AQUISIZIONE E STAMPA DI UNA STRINGA

.data
	
	hello:	.string	"Inserisci una frase...\n"
	
	lung = .-hello
	
	stringa:	.space	128		#grandezza spazio da allocare per la stringa (lunghezza massima stringa)
	
	lung: .long 0
	
.text

	.global	main
	
main:

// LEGGO una STRINGA da terminale

		movl		$4, %eax
		movl		$1, %ebx
		movl		$hello, %ecx
		movl		$lung, %edx
		int		$0x80

		movl		$3, %eax		#read --> scanf in c
		movl		$0, %ebx
		movl		$stringa, %ecx
		movl		$128, %edx
		int		$0x80
		
// quando viene eseguita la READ, nel registro eax viene salvata la DIMENSIONE EFFETTIVA dei caratteri inseriti comprensivo del '\n'

// SALVO il contenuto di EAX dentro LUNG

		movl		%eax, lung
		
// STAMPO la stringa	

		movl		$4, %eax
		movl		$1, %ebx
		movl		$stringa, %ecx
		movl		$lung, %edx
		int		$0x80
		
			//RETURN
			
		movl		$1, %eax
		movl		$0, %ebx
		int		$0x80
