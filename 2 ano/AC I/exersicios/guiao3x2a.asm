	.data
	
str1: .asciiz "Introduza um numero: \n "
str2: .asciiz "\nO valor em Binario: \n"
str3: .asciiz "0"
str4: .asciiz "1"
str5: .asciiz " "


	.eqv print_string,4
	.eqv read_int,5
	.eqv print_char,11
 	.eqv exit_program,10
	.text
	.globl main
	 
	
main:
	#str1
	la $a0,str1
	ori $v0,$0,print_string
	syscall
	
	#input int
	ori $v0,$0,read_int
	syscall
	move $t2,$v0 # value
		
	#str2
	la $a0,str2
	ori $v0,$0,print_string
	syscall
	
	
	
	li $t0,0#i = 0
	#li $t1,0 #soma
	li $t3,0x80000000#0x8
	#li $t4,0x0#test
for:   	bgt $t0,31,endf  #if the conditionn is true jump to the lable else continue
	
	
	
	#criar a variavel bit
	
	and $t4,$t2,$t3 # bit
	
	rem $t5,$t0,4
if2: 
	bne $t5,$0,endif2	
	
	la $a0,str5
	ori $v0,$0,print_string
	syscall
	
	j endif2
endif2:

	
if: 	bne $t4,$zero,else
	
	la $a0,str3#?????????
	ori $v0,$0,print_string
	syscall

	
	j endif
	
else:
	
	la $a0,str4#?????????
	ori $v0,$0,print_string
	syscall
	
endif:
	sll $t2, $t2, 1
	#soma
	addi $t0,$t0,1
	j for
endf:

	jr $ra
