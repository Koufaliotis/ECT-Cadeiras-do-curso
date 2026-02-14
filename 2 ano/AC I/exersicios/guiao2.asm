	.data
	
str1:   .ascii "my first string"
	.eqv print_string,4
	
	.text
	.globl main

	
main: 
	#ori $t0,$0,0x1234
	#ori $t1,$0,0x000f
	#and $t2, $t0, $t1
	#or $t3, $t0, $t1
	#nor $t4, $t0, $t1
	#xor $t5, $t0, $t1
	
	#negasao
	#ori $t0,$0,0x0614
	#nor $t1,$t0,$0
	#shift
	
	#li $t0,0xF
	
	#sll $t1,$t0,1
	#srl $t2,$t0,1
	#sra $t3,$t0,1
	
	# 2c
	#li $t0,0xF
	#sll $t1,$t0,1
	#xor $t2,$t0,$t1
	
	#gray exere
	#li $t0, 0xf
	#srl $t1,$t0,1
	#xor $t1,$t0,$t1
	
	
	#3c
	#la $a0,str1
	#ori $v0,$0,print_string
	#syscall
	
	jr $ra
