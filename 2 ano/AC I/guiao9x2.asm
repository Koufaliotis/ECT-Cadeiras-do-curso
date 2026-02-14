	.data
	
dle1:	.double 5.0
dle2:	.double 9.0
dle3:	.double 32.0

	.text
	.globl main
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	li $v0,7
	syscall
	mov.d $f12,$f0
	
	jal f2c
	
	mov.d $f12,$f0
	li $v0,3
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	
	jr $ra
	
f2c:
	la $t0,dle1
	l.d $f2,0($t0)		#//5.0
	
	la $t0,dle2
	l.d $f4,0($t0)		#//9.0
	
	la $t0,dle3
	l.d $f6,0($t0) 		#//32.0
	 
	#return
	sub.d $f0,$f12,$f6	# // (ft – 32.0)
	div.d $f2,$f2,$f4		# //  5.0 / 9.0
	
	mul.d $f0,$f2,$f0		# //return (5.0 / 9.0 * (ft – 32.0));
	
	jr $ra