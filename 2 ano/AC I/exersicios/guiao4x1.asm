	.data
	.eqv read_int,5
	.eqv read_string,8
	.eqv print_string,4
	.eqv print_int10,1
	.eqv SIZE, 20
str2:   .asciiz "\n numero de carecteres: "	
str3:   .asciiz "\n introduz a string: "
	
Array: .space 12
	
	.text
	.globl main
	
	
main:	
	# Mapa de registos 
	# num: $t0 
	# i: $t1 
	# str: $t2 
	# str+i:  $t3 
	# str[i]: $t4
	
	#printing str3
	la $a0,str3
	ori $v0,$0,print_string
	syscall
	
	la $a0,Array #this is the string of array
	li $a1,SIZE #size of string 		#the size must be size +1 to have he last empty
	li $v0,read_string
	syscall
	
	#saving array in $t4
	la $t4,Array 



#loop:
#    lb $t1, 0($t4)         # load character
#    beq $t1, $zero, end    # stop at null terminator
 #   move $a0, $t1
 #   li $v0, 11             # syscall: print_char
#    syscall
#    addi $t4, $t4, 1       # move to next character
#    j loop

#end:
#    li $v0, 10             # exit
#    syscall

	ori $t1,$0,0
	li $t2,0 #my counter
	
while: 
	lb $t3,0($t4) #array poiter that representes the memory of possion 0
	beq $t1,12,endwhile# str[i] != 0
	#la $t2,str
	
if:
	beq $t3,$0,endif
	addi $t2,$t2,1
	
endif:
	addi $t4,$t4,1
	addi $t1,$t1,1 
	
	j while
endwhile:

	move $a0,$t2
	ori $v0,$0,print_int10
	syscall
	jr $ra
