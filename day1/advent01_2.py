import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

with open('input.txt') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

	lines=np.sum(sliding_window_view(np.array(lines).astype(float), window_shape = 3), axis = 1)

	increases=0

	for index, elem in enumerate(lines):
		prev_el = float(str(lines[index-1]))
		curr_el = float(str(elem))

		if curr_el > prev_el:
			increases=increases+1

print(increases)