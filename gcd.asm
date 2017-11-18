	lw	0	1	a	load paramater b
	lw	0	2	b	load parameter a
	lw	0	4	gcdA	load gcd address
	jalr	4	7		call function gcd
	halt				halt program
gcd	lw	0	6	one
	lw	0	3	negPos	temporary use for negPos
loop	beq	1	2	exit	a == b goto exit
	nand	1	1	4	4 = ~a
	add	4	6	4	4 = -a
	add	2	4	5	5 = b - a
	nand	5	3	5
	nand	5	5	5	5 = (b - a) & negPos
cond	beq	5	0	LB	if b >= a goto LB
LA	nand	2	2	4	4 = ~b
	add	4	6	4	4 = -b
	add	1	4	1	a = a - b
	beq	0	0	loop
LB	add	2	4	2	b = b - a
	beq	0	0	loop
exit	add	0	0	3	clear return value
	add	3	1	3	ret = a
	jalr	7	6
one	.fill	1
negPos	.fill	-2147483648
gcdA	.fill	gcd
a	.fill	9999
b	.fill	3336