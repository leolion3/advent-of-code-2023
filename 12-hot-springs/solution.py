#!/usr/bin/env python3
import sys
from itertools import permutations, product, combinations


if len(sys.argv) < 2:
	exit(-1)

D = []
S = []

with open(sys.argv[1]) as f:
	for l in f.readlines():
		if not len(l):
			continue
		d, s = l.strip().split(' ')
		D.append(d)
		S.append(list(map(int, s.split(','))))


def comb(t):
	qm = [i for i, char in enumerate(t) if char == '?']
	pr = product('#.', repeat=len(qm))
	v = []

	for r in pr:
		c = list(t)
		for i, rep in zip(qm, r):
			c[i] = rep
		c = ''.join(c)
		v.append(''.join(c))
	return [list(filter(len, x.split('.'))) for x in list(set(v))]


p1 = 0
p2 = 0
lc = len(D)

for i, d in enumerate(D):
	print(f'Progress {i}/{lc}', end='\r')
	v = ['#' * j for j in S[i]]
	cm = comb(d)
	p1 += sum([1 for l in cm if l == v])
	cm = (comb(d + '?') * 5)[:-1]
	p2 += sum([len(l) ** len(v) for l in cm if l * 5 == v * 5])


print()
print('Solution 1:', p1)
print('Solution 2:', p2)