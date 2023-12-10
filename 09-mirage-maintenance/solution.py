#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	exit()

with open(sys.argv[1]) as f:
	data = f.readlines()


D = []
L = []


for line in data:
	_l = list(map(int, line.split(' ')))
	_d = _l
	d = []
	while True:
		_d = [_d[x + 1] - _d[x] for x in range(0, len(_d) - 1)]
		d.append(_d)
		if _d == ([0] * len(_d)):
			break
	D.append(d[::-1])
	L.append(_l)


S = []
for i, l in enumerate(L):
	v = 0
	for d in D[i]:
		v = v + d[-1]
	S.append(l[-1] + v)

print('Solution 1:', sum(S))


S = []
for i, l in enumerate(L):
	v = 0
	for d in D[i]:
		v = d[0] - v
	S.append(l[0] - v)

print('Solution 2:', sum(S))