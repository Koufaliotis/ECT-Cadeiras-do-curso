	.data
	
str:  	.asciiz "1982"
	
	
	.text
	.globl main
	
main: 
	addiu $sp,$sp,-4 #stack for ra
	sw $ra,0($sp)
	
	
	
	######
	la $a0,str
	jal atoi
	
	
	lw $a0,0($sp)
	li $v0,4
	syscall
	######
	jr $ra
	
	
atoi:
	#res: $v0
	#s: $a0
	#*s: $t0
	#digit: $t1
	
#this must be a function
#i need a main that inputs string "168638"
	li $v0,'0'
	

while: 
	lb $t0,0($a0)
	blt $t0,'0', endwhile
	bgt $t0,'9', endwhile
	
	addiu $a0,$a0,1
	li $t9,'0'
	
	sub $t1,$t0,$t9
	
	mul $v0,$v0,10
	
	add $v0,$v0,$t1
	

	j while
	
endwhile:
	
	jr $ra
#return result: good luck
