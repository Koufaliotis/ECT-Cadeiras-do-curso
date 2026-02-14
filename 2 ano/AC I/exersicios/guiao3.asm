	.data
str1: .asciiz "my string"
str2: .asciiz "my string2"
str3: .asciiz "my string3"	
	.text
	.globl main

main:
	
	li $t2,0 #i =0
	li $t0,0 #  somma =0
while: bge $t2,5, endw 	# while (i<5
		
	li $v0,4
	la $a0,str1
	syscall		#print string(str1)
	
	li $v0,5
	syscall #v0 ==5
		
	move $t1,$v0 #t1 == v0
		
		
		
if: 
	ble $t1, $0,else
	add $t0,$t0,$t1
		
	j endif
else:
	li $v0, 4
	la $a0,str2
	syscall
	
endif:
		
	addi $t2,$t2,1 # i++
	j while
endw:		
	li $v0,4
	la $a0,str3
	syscall
	
	li $v0,1
	move $a0,$t0
	syscall
	
	jr $ra
	
	
	
	
	