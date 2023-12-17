#!/usr/bin/env python3
import sys


if len(sys.argv) < 2:
	exit(-1)

with open(sys.argv[1]) as f:
	D = f.read().split('\n\n')


def cd(n1, n2):
	d = 0
	for i, e in enumerate(list(n1)):
		if n2[i] != e:
			d += 1
	return d == 1


def cm(n, p2):
	m = []
	for i, e in enumerate(n[:-1]):
		if e == n[i+1] or (p2 and cd(e, n[i+1])):
			m.append(i)
	for i in m:
		bad = 0
		f, l = i, i + 1
		while f >= 0 and l < len(n):
			if n[f] != n[l]:
				if p2 and cd(n[f], n[l]):
					bad += 1
				else:
					bad = 2
				if not p2 or bad > 1:
					break
			f -= 1
			l += 1
		else:
			if p2 and bad == 1 or not p2:
				return i + 1
	return 0


def hb(m, p2):
	return 100 * cm(m, p2)


def vb(m, p2):
	n = [''.join([x[i] for x in m]) for i in range(len(m[0]))]
	return cm(n, p2)

def sol(p2):
	s = 0
	for M in D:
		m = list(filter(len, M.split('\n')))
		v = vb(m, p2)
		h = hb(m, p2)
		s += v
		s += h
	return s

i = 1
for p2 in [False, True]:
	print('Solution', i, ':', sol(p2))
	i += 1