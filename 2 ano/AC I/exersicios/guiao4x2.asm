	.data
	.eqv print_int10
	.eqv SIZE, 4
	.eqv print_int10,1
	
Array:	.word 10,20,30,40 	
	
	.text
	.globl main

main:
	#t0 == i
	#t1 == Array
	#t2 == pointer
	#t3 == soma
	#
	#
	#
	
	
	la $t1, Array
	li $t3,0
for:
	bge $t0,SIZE,endfor
	lw $t2,0($t1)
	
	add $t3,$t3,$t2 #soma 
	
	addi $t1,$t1,4
	addi $t0,$t0,1
	j for
endfor:
	#print int
	move $a0,$t3
	ori $v0,$0,print_int10
	syscall
	jr $ra
	
