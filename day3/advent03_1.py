totals=[0,0,0,0,0,0,0,0,0,0,0,0]
with open('input.txt','r') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]
	div=len(lines) / 2
	gamma=""
	epsilon=""

	for line in lines:
		for i,elem in enumerate(list(line)):
			totals[i] += int(elem)

	for tot in (totals):
		if tot > div:
			gamma+=gamma.join('1')
			epsilon+=epsilon.join('0')
		else:
			epsilon+=epsilon.join('1')
			gamma+=gamma.join('0')

	answer=int(gamma,2)*int(epsilon,2)
	print(answer)