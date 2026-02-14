	.data
	
flt:	.float 1.0

	.text
	.globl main

main:
#input
#abs
#xtoy
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	li $v0,5 #x
	syscall
	
	move $a0,$v0
	
	li $v0,5 #x
	syscall
	
	move $t1,$v0 #y
	
	jal abs
	
	move $t0,$v0
	
	
	
	mtc1 $t0,$f2
	cvt.s.w $f12,$f2
	
	move $a0,$t1
	jal xtoy
	
	mov.s $f12,$f0
	li $v0,2
	syscall
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra

xtoy:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	mov.s $f2,$f12 # x
	move $t1,$a0	#y
	li $t0,0	#i
	
	
	la $t2,flt
	l.d $f4,0($t2) # result
	
	#abs(y)
	move $a0,$t1
	jal abs
	
	move $t3,$v0 #abs(y)
for1:
	beq $t0,$t3,endFor1
	
if1:
	ble $t1,0,else1
	mul.s $f4,$f4,$f2
	j endif1
else1:
	div.s $f4,$f4,$f2
endif1:	
	addi $t0,$t0,1
	j for1
endFor1:
	mov.s $f0,$f4
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
	
abs:
	addiu $sp,$sp,-4
	sw $ra,0($sp)
	
	move $t9,$a0
if:
	bgt $t9,0,endif
	mul $t9,$t9,-1
endif:
	move $v0,$t9
	
	lw $ra,0($sp)
	addiu $sp,$sp,4
	jr $ra
