	.data
str1: 	.asciiz "\n intoduza um numero: "
str2:	.asciiz "valor ignorado \n"
str3:	.asciiz "A soma dos positovos: "

	.eqv print_string,4
	.eqv read_int,5
	.eqv print_int,1
	.eqv exit_program,10
	.text
	.globl main

main: 	
	li $t1,0 # i = 0
	li $t2,0 # soma
	#for
for: bgt  $t1,5,endFor
	
	#vars
	la $a0 ,str1
	ori $v0,$0,print_string
	syscall
	
	ori $v0,$0,read_int
	syscall
	move $t0, $v0
	
		#if
if: 	blt $t0,0,else
	add $t2,$t2,$t0
	
	j endif	
		#else
else:
	la $a0 ,str2
	ori $v0,$0,print_string
	syscall
		#print str2
endif:
			
	la $a0 ,str3
	ori $v0,$0,print_string
	syscall
	# print str3
	move $a0,$t2
	ori $v0,$0,print_int
	syscall
	# print soma
	addi $t1,$t1,1
	j for
endFor:
	jr $ra	