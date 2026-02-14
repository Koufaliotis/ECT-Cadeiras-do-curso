	.data
	.eqv print_string,4
	.eqv print_char,11
	.eqv size,3
strArray: .word str1,str2,str3	#the array will use 4 bytes

str1: 	.asciiz "test1"
str2:	.asciiz "test2"
str3:	.asciiz "test3"
	.text
	.globl main
#incrementacao de 4?
#
main:
	# t0 = i
	# t1 = array
	# 
	#
	#
	#
	#
	li $t0,0
for:
	beq $t0,size,endFor
	la $t1,strArray
	sll $t2,$t0,2 # offset left by 2
	addu $t2,$t1,$t2#  ??????????????????????
	lw $a0,0($t2)
	li $v0,print_string
	syscall
	
	li $a0,'\n'
	li $v0,print_char	
	syscall
	
	
	addi $t0,$t0,1
	j for
endFor:

