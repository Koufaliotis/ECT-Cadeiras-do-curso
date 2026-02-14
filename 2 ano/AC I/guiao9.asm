	.data
	
	.eqv read_int,5
	.eqv print_float,2	
	
ct1: 	.float 2.59375
ct2:	.float 0.0

	.text
	.globl main
	
main:

do:
	li $v0,read_int
	syscall
	move $t0,$v0
	
	la $t1,ct1 #access float form copros
	l.s $f0,0($t1)#make it 2.59375
	
	mtc1 $t0,$f4
	cvt.s.w $f4,$f4 # (float)val????????????  makes it float
	
	mul.s $f12,$f0,$f4
	
	li $v0,print_float
	syscall
	
	la $t1,ct2
	l.s $f2,0($t1)
	c.eq.s $f12,$f2
	bc1f do
	
	
	li $v0,0
	jr $ra
