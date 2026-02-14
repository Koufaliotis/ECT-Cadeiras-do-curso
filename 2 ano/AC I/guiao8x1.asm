	.data
	
str: 	.asciiz "1944"
	
	.text
	.globl main

main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	la $a0,str
	jal atoi
	
	move $a0,$v0
	li $v0,1
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	
	jr $ra

atoi:

	li $v0,0
while:
	lb $t0,0($a0)
	blt $t0,'0',endwhile
	bgt $t0,'9',endwhile
	
	addiu $a0,$a0,1
	
	li $t9,'0'
	sub $t1,$t0,$t9
	
	mul $v0,$v0,10
	add $v0,$v0,$t1

	
	j while

endwhile:

	
	jr $ra