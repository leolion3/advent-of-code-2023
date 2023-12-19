#!/usr/bin/env python3
import sys


if len(sys.argv) < 2:
	exit(-1)

with open(sys.argv[1]) as f:
	m = list(filter(len, f.read().split('\n')))
	cols = [[x[i] for x in m] for i in range(len(m[0]))]


def shift(p2):
	for c in cols:
		for _ in range(c.count('O')):
			j = len(c) - 1
			while j > 0:
				if c[j] == 'O' and c[j-1] == '.':
					c[j] = '.'
					c[j-1] = 'O'
				j -= 1
	if not p2:
		return
	for c in cols:
		for _ in range(c.count('O')):


def s():
	s = 0
	for c in cols:
		for i in range(len(c))[::-1]:
			if c[len(c) - i - 1] == 'O':
				s += i+1
	return s


