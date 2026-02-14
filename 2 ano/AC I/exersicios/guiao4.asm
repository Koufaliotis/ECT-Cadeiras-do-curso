	.data
str:	.space 12
	.align 2 # 2^x x=2
a:	.space 48 #12 innteiros
	.text
	.globl main
	
main:
	
	
	li $t0,0
	
for1:
	bge $t0,12,endfor1
	la $t3,str		# ps =str
	addI $t3,$t3,$t0		# ps=str(i)
	lb $t2,0($t3)

	
	la $t4,a		#p1 = 	
	sll $t9,$t0,2		#ttt = i *4	
	addu $t0,$t0,1		# pi =pi +(i * 4)
	lw $t1, 0($t4)		#temp1 = a(i)
	
	j for


endfor1:
#------------------------------------------------------------------------------------------------------------

	la $t3,str	#ps = str
	addiu $t3,$t5,12 #paf = str + 12
	
for2:
	bgeu $t3,$t5,endfor2
	lb $t2, 0($t3)		#tmp = *ps
	
	addiu $t3, $t3,1
	j for2
	
endfor2:


#-----------------------------------------------------------------------------------------------------z
	
	
	
	
	
	
	
endfor2:
