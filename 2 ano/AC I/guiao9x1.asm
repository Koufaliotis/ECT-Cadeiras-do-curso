	.data
	
fl1:	.float 0.0 #res
fl2:	.float 2.59375 # constatnt

	.text
	.globl main
	
main:
	
	li $t0,0	
do:
	li $v0,5		# //val read_int()
	syscall
	move $t0,$v0
	
	#create a f0 = f2
	la $t1,fl2
	l.s $f0,0($t1)
	#(float)val
	mtc1 $t0,$f4 #transfers the $t0 in %f4
	cvt.s.w $f4,$f4		# //(float)val
	
	mul.s $f12,$f4,$f0		#//res = (float)val * 2.59375 $f12 its like la $a0 for float
	
	#move $a0,$f6
	li $v0,2
	syscall 		#//print_float(val)
	
	#create f1
	la $t2,fl1
	l.s $f2,0($t2)
	
	c.eq.s $f12,$f2
	bc1f do			#//while(res != 0.0);
	
	jr $ra