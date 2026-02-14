	.data
# not finished and has erros
#//Darr:	.space 64
Darr:	.double 1.0,1.2,1.3,1.4
dbl:	.double 0.0

Dconst1: .double -1.0
Dconst2: .double 1.0

	.text
	.globl main
main:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	li $t0,0
	
	la $t1,Darr
for1:
	beq $t0,4,endFor1
	
	l.d $f2,0($t1)
	mov.d $f12,$f2 # zee double//
	
	move $a0,$t0
	
	jal max
	
	addiu $t1,$t1,8	
	addi $t0,$t0,1
	j for1
endFor1:
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
	
	
max:
	mov.d $f2,$f12	# p
	move $t2,$a0 	# n
	
	mtc1 $t2,$f4
	cvt.d.s $f4,$f4
	
	sub.d $f4,$f4,Dconst1
	add.d $f4,$f4,$f2# u
	
	add.d $f8,$f2,Dconst2 #max
for2:
	bgt $f2,$f4,endFor2 
	
if:
	bc1t $f2,$f8,end

end:	
	
	addi $f2,$f2,Dconst2
	j for
endFor2:
	