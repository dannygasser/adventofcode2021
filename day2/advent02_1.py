with open('input.txt') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

	totals={}
	totals['forward']=0
	totals['down']=0
	totals['up']=0

	for elem in (lines):
		direction,val=elem.split(' ')
		totals[direction]+=int(val)

	depth=totals['down'] - totals['up']

	position=totals['forward']*depth
		
	print(position)