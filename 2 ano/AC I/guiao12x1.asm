########################################
#						align	size	offset
# unsigned int id_number			4	4	0
#						1	18	4
#						1	15	22
#						4	4	40
#						4	44	--
	.data
	
str:	.asciiz "a"
	.align 2
st_ar:	.space 176 #??????????
grade:	.space 4
	
	.text
	.globl main
	
main:

	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	
	
	
	
	la $a0,st_ar
	li $a1,4
	jal read_data
	la $a0,st_ar
	li $a1,4
	la $a2,media
	jal max
	move $t0,$v0
	li $v0 ,4
	la $a0, str
	syscall
	move $a0,$t0
	jal print_student

	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
	
	
########################################################
	.data
	
rdStr1  .asciiz "a"
rdStr2: .asciiz "a"
rdStr3: .asciiz "a"
rdStr4: .asciiz "a"

	.text

read_data:
	move $t1,$a0
	move $t2,$a1
	li $t0,0
rd_w1:
	beq $t0,$t2,rd_ew
	
	li $v0,4
	la $a0,rdStr1
	syscall
	
	mul $t4,$t0,44
	addu $t4,$t1,$t4
	li $v0,5
	syscall
	sw $v0,0($t4)
	
	li $v0,4
	la $a0,rdStr2
	syscall
	
	li $v0,0
	addiu $a0
	####+++++++++more in phone
	addi $t0,$t0,1
	j rd_w1

rd_ew:

	