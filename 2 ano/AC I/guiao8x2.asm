	.data

str1:	.asciiz "\ngive me a number n: "
str2:	.asciiz "\ngive me a base b: "
str: 	.space 32	
	.text
	.globl main
	
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	la $a0,str2
	li $v0,4
	syscall
	
	li $v0,5
	syscall
	move $a1,$v0 #b
	
	la $a0,str1
	li $v0,4
	syscall
	
	li $v0,5
	syscall
	#----------
	move $a0,$v0 #n
	la $a2,str   #str
	
	jal itoa
	
	move $a0,$v0
	li $v0,4
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra

itoa:
	addiu $sp,$sp,-20
	sw $s0,0($sp)
	sw $s1,4($sp)
	sw $s2,8($sp)
	sw $s3,12($sp)
	sw $ra,16($sp)
	
	
	move $s0,$a0 #n
	move $s1,$a1 #b
	move $s2,$a2 # p sw atr //char *p = s; 
	move $s3,$a2
	

Do:
	rem $t2,$s0,$s1 #resto //digit = n % b;
	div $s0,$s0,$s1 #      //n = n / b;
	
	move $a0,$t2
	jal toascii
	
	sb $v0,0($s2)
	addiu $s2,$s2,1	
			

	bgt $s0,$0,Do #	      // end do While
	
	sb $0,0($s2)
	move $a0,$s3
	jal strrev
	
	move $v0,$s3
	
	lw $s0,0($sp)
	lw $s1,4($sp)
	lw $s2,8($sp)
	lw $s3,12($sp)
	lw $ra,16($sp)
	addiu $sp,$sp,20
	
	jr $ra
##------------------------------
toascii:
	addiu $sp,$sp,-4
	sw $s4,0($sp)
	
	move $s4,$a0
	
	addiu $s4,$s4,'0' # v += '0';
if:
	ble $s4,'9',endIf       # if( v > '9' )
	addiu $s4,$s4,7	  #v += 7; // 'A' - '9' - 1 
endIf:
	move $v0,$s4
	
	lw $s4,0($sp)
	addiu $sp,$sp,4
	jr $ra
#-------------------------------	
strrev:
	addiu $sp,$sp,-12
	sw $s0,0($sp)
	sw $s1,4($sp)
	sw $s2,8($sp)
	
	move $s0,$a0  #may be i heve to change this $s0 to $t7!!!!!!
	move $s1,$a0
	move $s2,$a0
	
	
	
while1:
	
	lb $t1,0($s0)
	beq $t1,'\0',endWhile1
	

	
	
	addiu $s0,$s0,1  #you sould be at max - '\0'
	
	j while1
endWhile1:
	addiu $s0,$s0,-1 #good
	
while2:
	beq $s1,$s0,endWhile2 
	
	lb $t2,0($s0) #end
	lb $t3,0($s1) #start
	
	
	
	sb $t3,0($s0)#when is the change being made
	sb $t2,0($s1)#the chenge isnt made after the execution of the instruction
		     #some thing has a temp value
	
	addiu $s1,$s1,1
	addiu $s0,$s0,-1
	
	j while2
endWhile2:
	move $v0,$a0
	addiu $sp,$sp,12
	jr $ra 
