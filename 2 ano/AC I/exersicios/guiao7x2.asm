	.data
str:	.asciiz "paparia" 	

	.text
	.globl main
main:	
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	la $a0,str
	
	jal strrev
	
	move $a0,$v0
	li $v0,4
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	
	jr $ra

strrev:
	addiu $sp,$sp,-12
	sw $s0,0($sp)
	sw $s1,4($sp)
	sw $s2,8($sp)
	
	move $s0,$a0
	move $s1,$a0
	move $s2,$a0
	
	
	
while1:
	
	lb $t1,0($s0)
	beq $t1,'\0',endWhile1
	

	
	
	addiu $s0,$s0,1  #you sould be at max - '\0'
	
	j while1
endWhile1:
	addiu $s0,$s0,-1 #good
	
while2:
	beq $s1,$s0,endWhile2 
	
	lb $t2,0($s0) #end
	lb $t3,0($s1) #start
	
	
	
	sb $t3,0($s0)#when is the change being made
	sb $t2,0($s1)#the chenge isnt made after the execution of the instruction
		     #some thing has a temp value
	
	addiu $s1,$s1,1
	addiu $s0,$s0,-1
	
	j while2
endWhile2:
	move $v0,$a0
	addiu $sp,$sp,12
	jr $ra 
