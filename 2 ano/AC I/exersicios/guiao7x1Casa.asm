	.data
	
str1: 	.asciiz "Mpc_Master22"	
	.text
	.globl main
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)	
	
	la $a0,str1
	jal strcount
	
	move $a0,$v0
	li $v0,1
	syscall
	
	li $v0,0 #requierd
	
	
	lw $ra,0($sp) #must be this way
	addiu $sp,$sp,4
	
	
	jr $ra 

strcount:
	
	li $t1,0 #counter
for:	
	lb $t0,0($a0)
	addiu $a0,$a0,1
	beq $t0,'\0',endfor
	
	addi $t1,$t1,1
	
	j for
endfor:
	move $v0,$t1
	jr $ra

