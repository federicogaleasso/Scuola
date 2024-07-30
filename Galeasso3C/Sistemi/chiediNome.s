/*
Beniamino Galfre 3C
*/

.data
	stringa:					.space 128
	lungh:					.long 0
	domanda:			.string "come ti chiami ? \n"
	l = 								.-domanda
	buongiorno:		.string "buongiorno: "
	lun = 						.-buongiorno
	invio:						.string "\n"
	
.text
		.global main
	
main:
		movl	$4, %eax
		movl	$1, %ebx
		movl	$domanda, %ecx
		movl	$l, %edx
		int		$0x80

		movl	$3, %eax
		movl	$0, %ebx
		movl	$stringa, %ecx
		movl	$128, %edx
		int		$0x80
		
		movl	%eax, lungh
		
		movl	$4, %eax
		movl	$1, %ebx
		movl	$buongiorno, %ecx
		movl	$lun, %edx
		int		$0x80
		
		movl	$4, %eax
		movl	$1, %ebx
		movl	$stringa, %ecx
		movl	lungh, %edx
		int		$0x80
		
		movl	$4, %eax
		movl	$1, %ebx
		movl	$invio, %ecx
		movl	$2, %edx
		int		$0x80
		
		movl	$1, %eax
		movl	$0, %ebx
		int		$0x80

