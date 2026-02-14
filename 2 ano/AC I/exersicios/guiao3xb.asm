	.data
str1: 	.asciiz "introduza um numero"
str2: 	.asciiz "\nO valor em binario"
char1:	.byte '1'
char2:	.byte '0'

	.eqv print_string,4
	.eqv print_int,1
	.eqv read_int,5
	.eqv print_char,11
	.eqv exit_program,10
	
	.text
	.globl main
main:
	li $t0,0 # i = 0
	li $t1,0 #value
	li $t2,0 #bit
	
	la $a0, str1
	ori $v0,$0,print_string
	syscall
	
	ori $v0,$0,read_int
	syscall
	move $t1,$v0
	
	la $a0, str2
	ori $v0,$0,print_string
	syscall
	
	li $t3,0x80000000
	
	sll $t1,$t1,1
for:
	bge $t0,32,endfor
	

 	
	and $t2,$t1,$t3
if: 	
	bne $t2,0,else
	la $a0,char1
	ori $v0,$0,print_string
	syscall
	
	j endif
else:
	la $a0,char2
	ori $v0,$0,print_string
	syscall
	
endif:
	addi $t0,$t0,1
	j for
endfor:
	jr $ra 
	#for
