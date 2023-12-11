#!/usr/bin/env python3
import sys
import itertools


if len(sys.argv) < 2:
	exit(-1)

r = []
c = []
loc = []
img = []

with open(sys.argv[1]) as f:
	for i, l in enumerate(f.readlines()):
		if not len(l):
			break
		img.append(l)
		if not '#' in l:
			r.append(i)
			continue
		for j, e in enumerate(l):
			if e == '#':
				c.append(j)


def manhattan(p2, p1):
	x2,y2 = p2
	x1,y1 = p1
	d = abs((x2 - x1)) + abs((y2 - y1))
	return d


# Generate giant coordinates
def get_expanded(er):
	loc = []
	y = 0
	x = 0
	for i, l in enumerate(img):
		# Expand column
		if i in r:
			y += er
			continue
		# Expand row
		for j, e in enumerate(l):
			if j not in c:
				x += er
				continue
			else:
				x += 1
			if e == '#':
				loc.append((x, y))
		y += 1
		x = 0
	return loc

def sol_1():
	dist = []
	for pair in itertools.combinations(get_expanded(2), 2):
		p2, p1 = pair
		dist.append(manhattan(p2, p1))
	return sum(dist)


def sol_2():
	dist = []
	for pair in itertools.combinations(get_expanded(1000000), 2):
		p2, p1 = pair
		dist.append(manhattan(p2, p1))
	return sum(dist)


print('Solution 1:', sol_1())
print('Solution 2:', sol_2())
#print('\n'.join(fex))