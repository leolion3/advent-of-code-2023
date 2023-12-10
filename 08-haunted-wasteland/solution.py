#!/usr/bin/env python3
import sys
from math import lcm


if len(sys.argv) < 2:
	exit()

loc = {}

with open(sys.argv[1]) as f:
	path = list(f.readlines(1)[0].rstrip())
	data = f.read()
	for line in data.split('\n'):
		if not len(line):
			continue
		line = list(filter(len, line.replace(' = (', ',')
						   .replace(')',',')
						   .replace(' ',',')
						   .split(',')))
		loc[line[0]] = {
			'L': line[1].strip(),
			'R': line[2].strip()
		}


def get_path(c):
	global path
	p = path
	l = 0
	while not c[-1] == 'Z':
		e = p[0]
		p = p[1:]
		if not len(p):
			p = path
		c = loc.get(c)[e]
		l += 1
	return l


def sol_2():
	global path, loc
	x = [x for x in loc.keys() if x[-1] == 'A']
	lens = [get_path(a) for a in x]
	return lcm(*lens)


print('Solution 1:', get_path('AAA'))
print('Solution 2:', sol_2())
