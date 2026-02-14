	.data
	
	.eqv TRUE,1
	.eqv FALSE,0
	.eqv SIZE,10
	
array:	.word 1,5,9,8,3,4,6,7,2 	
	.text
	.globl main

main:
	#$t0 = i
	#$t1 = top
	#$t2 = array
	#$t3 = p
	#$t4 = p + 1
	#$t5 = bool
	li $t5,0
while:
	beq $t5,1,endWhile
	
	li $t5,0
	li $t0,0
	
	la $t2,array
for:
	bgt $t0,7,endfor
	lw $t3,0($t2)
	#addi $t2,$t2,4
	lw $t4,4($t2)
	
	
	
if:
	bge $t3,$t4,else
	#brake
	j endif
else:
	##do the chage
	sw $t3,4($t2) #becase p + 1
	#addi $t2,$t2,-4
	sw $t4,0($t2) #for p
	li $t5,1
endif:
	addi $t0,$t0,1
	addi $t2,$t2,4 #for array[i + 1]
	
	j for

endfor:
	
	j while
endWhile:
	jr $ra