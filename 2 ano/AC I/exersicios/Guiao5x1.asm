	.data
	.eqv read_int,5 #print str
	.eqv print_int,1
	.eqv SIZE,10
	
Array:  .word 40
	.text
	.globl main
	#make int array and 
	#make a program that reads and put a int in to a array until the array is full
main:
	#t0 == i
	#t1 == Array
	
	la $t1,Array
	
for:
	beq $t0,SIZE,endFor
	lw $t2,0($t1)
	
	#li $a0,$t3
	ori $v0,$0,read_int
	syscall
	
	sw $v0,0($t1)
	
	addi $t1,$t1,4
	addi $t0,$t0,1
	j for
endFor:
	
	jr $ra
	
