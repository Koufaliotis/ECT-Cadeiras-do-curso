	.data
str1: .asciiz "introdusa 2 numeros: "
str2: .asciiz "A soma dos dois numeros e': "
	.eqv print_string,4 #creatin of a constan
	.eqv read_int,5 #?
	.eqv print_int,1
	.eqv read_int10,1#??
	#.eqv exit_
	.text
	.globl main
main: 	la $a0,str1
	ori $v0,$0,print_string
	syscall #print str1
	
	
	ori  $v0,$0,read_int
	syscall #transfera o valor de int para $v0
	move $t0,$v0
	
	
	ori $v0,$0,read_int
	syscall
	move $t1,$v0
	
	
	#or $t0,$v0,$0 i dont know if i need it
	
	addi $t2,$t1,$t0
	
	#printing string
	la $a0,str2
	ori $v0,$0,print_string
	syscall
	
	move $a0,$t2
	ori $v0,$0,print_int
	syscall
	
	jr $ra
