#!/usr/bin/env python3
import sys
import copy


if len(sys.argv) < 2:
	exit(-1)

tm = {
	(-1, 0): {
		'from': ['S', '|', 'L', 'J'],
		'to': ['F', '|', '7']
	},
	(1, 0): {
		'from': ['S', '|', '7', 'F'],
		'to': ['|', 'L', 'J']
	},
	(0, -1): {
		'from': ['S', '-', 'J', '7'],
		'to': ['-', 'F', 'L'],
	},
 	(0, 1): {
 		'from': ['S', '-', 'F', 'L'],
 		'to': ['-', '7', 'J']
 	}	
}

M = []
S = (0, 0)

with open(sys.argv[1]) as f:
	for i, _l in enumerate(f.readlines()):
		M.append(list(_l.strip()))
		if 'S' in _l:
			S = (i, _l.index('S'))
T = copy.deepcopy(M)


def get_traverseable(y, x, yn, xn, _next):
	global T
	c = T[y][x]
	_traverseable = []
	for (yy, xx) in _next:
		if yn < 0 or yn >= len(T) or xn < 0 or xn >= len(T[0]):
			continue
		if c in tm[(yy, xx)]['from'] and T[yn][xn] in tm[(yy, xx)]['to']:
			_traverseable.append((yy, xx))
	return _traverseable


def get_next(y, x):
	global T
	bm = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	_C = [(y + yy, x + xx) for (yy, xx) in bm if (yy, xx) in get_traverseable(y, x, y+yy, x+xx, bm)]
	C = []
	for cy, cx in _C:
		if cy >= 0 and cy < len(T):
			if cx >= 0 and cx < len(T[cy]):
				if T[cy][cx] in ['|', '-', 'L', 'J', '7', 'F']:
					C.append((cy, cx))
	return C


LT = []

def traverse():
	global T, LT, S
	ans = []
	i = 1
	y, x = S
	LT.append((y,x))
	_next = get_next(y, x)
	while len(_next) > 0:
		t = []
		for (yy, xx) in _next:
			LT.append((yy, xx))
			if T[yy][xx] == 'S':
				continue
			t.extend(get_next(yy, xx))
			T[yy][xx] = f'o'
		ans.append(i)
		_next = t
		if not len(t):
			break
		i += 1
	return max(ans)


def mark_enclosed():
	global M, LT
	gc = 0
	for i, l in enumerate(M):
		for j, e in enumerate(M[i]):
			if (i, j) in LT:
				continue
			yi = i + 1
			xi = j + 1
			count = 0
			while yi < len(M):
				while xi < len(M[i]):
					# L and 7 do not enclose element, scan for horizontal enclosure
					if (yi, xi) in LT and M[yi][xi] not in ['.', 'L', '7']:
						count += 1
					xi += 1
					break
				yi += 1
			if count % 2 != 0:
				gc += 1
				M[i][j] = 'x'
	return gc

print('Solution 1:', traverse())
print('Solution 2:', mark_enclosed())

#for l in M:
#	print(' '.join(l))