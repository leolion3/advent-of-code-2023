#!/usr/bin/env python3

def get_code(entry):
	# Find first number
	first, last = None, None
	for c in entry:
		if c.isdigit():
			first = c
			break
	# Find last number
	for c in entry[::-1]:
		if c.isdigit():
			last = c
			break
	first = first or '0'
	last = last or '0'
	return ''.join([first, last])


with open('input.txt') as f:
	print(sum([int(get_code(entry)) for entry in f.readlines()]))