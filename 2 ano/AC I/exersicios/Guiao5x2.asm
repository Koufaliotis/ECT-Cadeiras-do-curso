	.data
	.eqv SIZE,10 
	.eqv print_string,4
	.eqv print_int,1
intArray: .word 8,-4,3,5,124,-15,87,9,27,15
str1: .ascii "printing Array: "
str2: .ascii ", "
	.text
	.globl main
	
main:
	# t0 = i
	# t1 = poiter of intArray
	# t2 =  
	# t3 =
	# t4 =
	
	la $t1,intArray
	
	lw $t2,0($t1)
	
	la $a0,str1
	li $v0,print_string
	syscall
	
for:
	beq $t0,SIZE,endFor
	lw $t2,0($t1)
	
	or $a0,$t2,$0
	li $v0,print_int
	syscall
	
	la $a0,str2
	li $v0,print_string
	syscall
	
	addi $t0,$t0,1
	addi $t1,$t1,4
	j for
endFor:

	jr $ra