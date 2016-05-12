#! /usr/bin/python

# I'm editing this file for the pulling competency

from __future__ import print_function
import copy
import random

time_limit = 20 # the number of time steps to simulate
size = 9 # the width and height of the simulation area in blocks
stencil = {(u, v) for u in range(-1, 2) for v in range(-1, 2) if (u, v) != (0, 0)}

def get_neighbors(point):
	result = set()
	for offset in stencil:
		x = point[0] + offset[0]
		if x >= 0 and x < size:
			y = point[1] + offset[1]
			if y >= 0 and y < size:
				result |= {(x, y)}
	return result

zones = [' ', 'I', 'R', 'C'] # empty, industrial, residential, commercial

city = [[random.choice(zones) for y in range(size)] for x in range(size)]

for step in range(time_limit):
	new_city = copy.deepcopy(city)
	for x in range(size):
		for y in range(size):
			new_city[x][y] = city[x][y] # the default is that cells don't change
			blocks = 0
			for neighbor in get_neighbors((x, y)):
				if new_city[neighbor[0]][neighbor[1]] == ' ':
					blocks += 1
			if city[x][y] != ' ':
				if city[x][y] == 'R':
					if blocks >= 5:
						new_city[x][y] = 'C'
				if city[x][y] == 'I':
					if blocks >= 4:
						new_city[x][y] = 'R'
				if blocks == 0:
						new_city[x][y] = ' '	
			if city[x][y] == ' ':
				if blocks == 1 or blocks == 0:
					new_city[x][y] = 'I'			

	print('Step {step}:'.format(step = step))
	for y in reversed(range(size)):
		print('  ', end = '')
		for x in range(size):
			print(new_city[x][y], end = '')
		print()
	print()
	city = new_city
