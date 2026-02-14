#$a0 = fazem parte para a cria;ao de funcoes 
#$a1 =

#a recebe e func retorna em v
#criar uma stack e pomos la as variaveis da funcao e no fim da funcao "limpamos" a memoria ou pomos o estado inicial


	.data
	
str:	.asciiz "tiheraujrw eha gujoref"
	.text
	.globl main

main: 
	addiu $sp,$sp,-4 #why -4 because you go back and get void ????????????
	sw $ra,0($sp)
	
	la $a0,str
	jal strlen	#calls then func #what ever reteunrs in the func 

	move $a0,$v0	
	li $v0,1
	syscall
	
	li $v0,0
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
	
strlen: 		#int stringlen(char *a)
	li $t0,0	#len = 0
str1_w1:
	lb $t1,0($a0)	# aux = *s
	addiu $a0,$a0,1 #s**
	beq $t1,$0,str1_ew1
	
	addi $t0,$t0,1
	
	
	
	j str1_w1
str1_ew1:

	move $v0,$t0
	
	jr $ra	#returns $v0