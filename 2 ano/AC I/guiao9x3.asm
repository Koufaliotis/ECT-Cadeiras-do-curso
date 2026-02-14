	.data

#//Darr:	.space 64
Darr:	.double 1.0,1.2,1.3,1.4
dbl:	.double 0.0

	.text
	.globl main
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)

	la $a0,Darr
	li $a1,4 #array size
	jal average
	
	mov.d $f12,$f0
	li $v0,3
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra

average:
	move $t1,$a0 # array
	move $t0,$a1 # n
	
	
	la $t2,dbl
	l.d $f2,0($t2) 	# //sum
	
	addi $t0,$t0,-1 		# // int i = n-1; 
for:				# // for(; i >= 0; i--)
	blt $t0,0,endFor
	
	l.d $f4,0($t1)		
	
	add.d $f2,$f2,$f4 	# // sum += array[i];
	
	
	addiu $t1,$t1,8
	addi $t0,$t0,-1
	j for
endFor:
	
	mtc1 $a1,$f6
	cvt.d.w $f6,$f6
	
	div.d $f0,$f2,$f6
	
	
	
	jr $ra