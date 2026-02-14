 	.data  # nada a colocar aqui, de momento 
 	.text 
 	.globl main 
main: 
#	ori $t0,$0,10 # $t0 = x (substituir val_x pelo 
# 	#add $t0,$t0,3		# valor de x pretendido) 
# 	ori $t2,$0,8 # $t2 = 8 
# 	add $t1,$t0,$t0 # $t1 = $t0 + $t0 = x + x = 2 * x 
# 	add $t1,$t1,$t2 # $t1 = $t1 + $t2 = y = 2 * x + 8 
#exer2 	
 	ori $t3,$0,5
 	ori $t4,$0,8
 	mul $t3,$t3,2
	sub $t5,$t3,$t4

  	jr $ra # fim do programa?????????
