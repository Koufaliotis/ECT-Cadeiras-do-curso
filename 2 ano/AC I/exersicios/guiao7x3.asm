	.data
	
str1:	.asciiz "la bola"
str2:	.space 20
	.asciiz ""
	
	.text
	.globl main
	
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	la $a0,str1
	la $a1,str2
	
	jal cpyStr
	
	move $a0,$v0	
	li $v0,4
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
	
cpyStr:
	addiu $sp,$sp,-8
	sw $s0,0($sp)
	sw $s1,4($sp)
	
	
	move $s0,$a0
	move $s1,$a1
	
while:
	
	
	lb $t1,0($s0)
	sb $t1,0($s1)
	
	addiu $s0,$s0,1
	addiu $s1,$s1,1
	
	beq $t1,'\0',endWhile
	j while
endWhile:
	sb $0,0($s1)
	
	
	lw $s0,0($sp)
	lw $s1,4($sp)
	
	move $v0,$a1
	
	addiu $sp,$sp,8
	jr $ra