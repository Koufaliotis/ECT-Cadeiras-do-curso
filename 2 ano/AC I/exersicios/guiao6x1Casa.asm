	.data
	
array: 	.word str1,str2,str3

str1:	.ascii "Array"
str2:	.ascii "de"
str3:	.ascii "ponteiros"
	
	
	.eqv print_string,4
	
	.text
	.globl main
	
main:
	#$ $t0 = array
	#  $t1 = i
	#  $t2 = word of array
	
while:
	#condition ? maybe auntil poiter == '/0'
	beq $t1,3,endwhile
	
	la $t0,array
	sll $t2,$t1,2# shift mem value x 4 helps to access the word of the array as pointer
	
	addu $t2,$t0,$t2 #access the array[i] 
	
	lw $a0,0($t2)
	li $v0,print_string
	syscall
	
	li $a0,'\n'
	li $v0,print_string	
	syscall
	
	addi $t1,$t1,1
	
	j while
endwhile:
	
	#brake it to char
	
	#print 
