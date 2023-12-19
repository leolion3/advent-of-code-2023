#!/usr/bin/env python3
import sys


if len(sys.argv) < 2:
	exit(-1)

with open(sys.argv[1]) as f:
	vals = f.readlines()[0].strip().split(',')


def hash(val):
	s = 0
	for c in list(val):
		s += ord(c)
		s *= 17
		s %= 256
	return s


def sol_1():
	global vals
	i = 0
	for val in vals:
		i += hash(val)
	return i


def sol_2():
	global vals
	boxes = {}
	focals = {}
	for val in vals:
		if '-' in val:
			lbl = val[:-1]
			op = val[-1]
		else:
			lbl, fl = val.split('=')
			op = '='
		box = hash(lbl)
		lenses = boxes.get(box)
		if op == '-':
			if lenses and lbl in lenses:
				del focals[(box, lbl)]
				lenses.remove(lbl)
				boxes[box] = lenses
		elif op == '=':
			if not lenses:
				boxes[box] = [lbl]
				focals[(box, lbl)] = int(fl)
			elif not lbl in lenses:
				lenses.append(lbl)
				boxes[box] = lenses
				focals[(box, lbl)] = int(fl)
			elif lbl in lenses:
				focals[(box, lbl)] = int(fl)
	s = 0
	i = 1
	for box, lenses in boxes.items():
		if not len(lenses):
			continue
		for j, lbl in enumerate(lenses):
			s += (box+1) * (j+1) * focals[(box, lbl)]
		i += 1
	return s


print('Solution 1:', sol_1())
print('Solution 2:', sol_2())