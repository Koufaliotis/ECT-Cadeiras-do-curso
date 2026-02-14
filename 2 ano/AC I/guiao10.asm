	.data
fl1:   	.float 1.0
	um double tem 8 bytes
	.text
	.globl main
	
main:
	addi $sp,$sp,-4
	lw $ra,0($sp)
	
	
	li $t0,2 #why 2:so the float can be 2.0 
	mtc1 $t0,$f12
	cvt.s.w $f12,$f12 #x
	
	li $a0,4 #y
	
	jal floatxtoy

	
	addi $sp,$sp,4
	lw $ra,0($sp)
	
	jr $ra

floatxtoy:
	addi $sp,$sp,-12
	sw $s0,0($sp) 	
	s.s $f20,4($sp)
	sw $ra,8($sp)
	
	move $s0,$a0#y
	mov.s $f20,$f12#x
	
	
	
	li $t0,0
	
	#if $a0 = y
	j abs#here it goes
	li $t1,$v0 #|y|
	
	
for:

	bne $t0,0,endfor
	bne $f20,1.0,endofor
	beq $t0,$t1,endfor #abs(y) is neede
	
if1:	
	blt $s0,$0,else1
	la $a0,
	mul.s $f20,$f20,fl1
	j endif1
else1:


endif1:


endfor:	

	jr $ra

	
			
abs:	
	li $t2,$a0
if2:
	bgt $t2,0,else
	mul $t2,$t2,-1
	j endif2
	
	
endif2:
	move $v0,$t2
	jr $ra

