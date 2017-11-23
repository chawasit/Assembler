	lw	0	2	mcand
	lw	0	4	mcomp
	lw	0	3	mplier
loop	nand	3	4	5	# 5 = ~(mcomp & mplier)
	nand	5	5	6	# 6 = mcomp & mplier
	beq	6	0	shift	# jump if 6 is zero
sum	add	1	2	1	# add mcand to result(1)
	nand	5	3	3	# mplier = mplier - mcomp
	nand	3	3	3	# mplier = mplier - mcomp
shift	add	2	2	2	# shift left mcand
	add	4	4	4	# shift left mcomp
	beq	3	0	exit	# if mplier is zero then exit
	beq	0	0	loop
exit	halt
mcand	.fill	32766
mplier	.fill	10383
mcomp	.fill	1
