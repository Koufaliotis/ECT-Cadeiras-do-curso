	.data
str1: 	.asciiz "\n Nmec:"
str2: 	.asciiz "\n Nmec:"
str3:  	.asciiz "\n Nmec:"

#-------------------------------
stg:	.word 72343
	.asciiz "Napoleao"
	.space 9
	.asciiz "Bonaparte"
	.space 5	
	.float 5.1



	.text
	.globl main
#-------------------------------
main:
	
	la $t0,stg # load int //also sets $t0 at possion of truct
	
	la $a0,str1
	li $v0,4
	syscall
	
	li $v0,36
	lw $a0,0($t0)
	syscall#??????????????????????????? que print vai fazer 36 ou 72343
	
	la $a0,str2
	li $v0,4
	syscall
	
	li $v0,4
	addiu $a0,$t0,22     #shifts the memmory
	syscall #print last name
	
	#li $v0,11
	#li $a0,$t0
	#syscall
	
	li $v0,11
	li $a0,','
	syscall #print (',')
	
	la $a0,str3
	li $v0,4
	syscall #print str3
	
	l.s $f12,40($t0)
	
	
	#objective print it how i dont know
	#syscall
	
	
	
	
	jr $ra