with open('input.txt') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

	totals={}
	totals['forward']=0
	totals['depth']=0

	aim=0

	for elem in (lines):
		direction,val=elem.split(' ')
		if direction=='down':
			aim+=int(val)
		elif direction=='up':
			aim-=int(val)
		elif direction=='forward':
			totals['forward']+=int(val)
			totals['depth']+=aim*int(val)

	position=totals['forward']*totals['depth']
		
	print(position)