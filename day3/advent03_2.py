totals=[0,0,0,0,0]	
with open('input.txt','r') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

for line in lines:
	for i,elem in enumerate(list(line)):
		totals[i] += int(elem)

oxygen=lines.copy()
co2=lines.copy()

for i,tot in enumerate(totals):
	if tot >= len(oxygen)/2:
		for val in oxygen:
			if val[i] == '0':
				oxygen.remove(val)
	if tot >= len(co2)/2:
		for val in co2:
			print('val=',val[i])
			if val[i] == '1':
				print('i=',i)
				#print('co2',tot,val)
				co2.remove(val)

a='hello'
print(a[0])
print(oxygen)
print(co2)