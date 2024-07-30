// prova

.data
		readNome:	.space 128
		lungh1:	.long 0
		
		readCog:	.space 128
		lungh2:	.long 0
		
		nome:	.string "Inserisci il tuo nome\n"
		dim_nome=	.-nome
		
		cog:	.string "Inserisci il tuo cognome\n"
		dim_cog=	.-cog
		
		ug:	.string "Le due stringhe sono uguali\n"
		dim_ug=	.-ug
		
		div:	.string "Le due stringhe sono diverse\n"
		dim_div=	.-div
		
.text

		.global	main
		
main:

cheidiNome:
	movl	$4, %eax
	movl	$1, %ebx
	movl	$nome, %ecx
	movl	$dim_nome, %edx
	int	$0x80
	
	movl	$3, %eax
	movl	$1, %ebx
	movl	$readNome, %ecx
	movl	$128, %edx
	int	$0x80
	
	movl %eax, lungh1

cheidiCog:	
	movl	$4, %eax
	movl	$1, %ebx
	movl	$cog, %ecx
	movl	$dim_cog, %edx
	int	$0x80
	
	movl	$3, %eax
	movl	$1, %ebx
	movl	$readCog, %ecx
	movl	$128, %edx
	int	$0x80
	
	movl %eax, lungh2

stampaNome:
	movl	$4, %eax
	movl	$1, %ebx
	movl	$readNome, %ecx
	movl	$128, %edx
	int	$0x80

stampaCog:
	movl	$4, %eax
	movl	$1, %ebx
	movl	$readCog, %ecx
	movl	$128, %edx
	int	$0x80

compara:
	movl	$10, %eax
	movl 	$10, %ebx
	cmpl	%eax, %ebx
	je		uguale
	jne		diverso
	
uguale:
	movl	$4, %eax
	movl	$1, %ebx
	movl	$ug, %ecx
	movl 	$dim_ug, %edx
	int		$0x80
	jmp		fine

diverso:	
	movl 	$4, %eax
	movl 	$1, %ebx
	movl	$div, %ecx
	movl	$dim_div, %edx
	int		$0x80
	
fine:	
		//RETURN
	movl	$1, %eax
	movl	$0, %ebx
	int	$0x80
