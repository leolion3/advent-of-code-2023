#!/usr/bin/env python3
import re

with open('input.txt') as f:
	data = f.readlines()
	#data = re.sub('[^a-zA-Z0-9*\n]', '.', f.read())

adj_matrix = [['0' for _ in range(len(data[0]))] for _ in range(len(data))]


def extract_number(row, idx):
	number = ''
	while row[idx].isdigit():
		number += row[idx]
		idx += 1
	return number


def build_matrix():
	global adj_matrix, data
	y = 0
	for row in data:
		x = 0
		while x < len(data[y]):
			col = data[y][x]
			if col.isdigit():
				number = extract_number(row, x)
				for i in range(len(number)):
					adj_matrix[y][x+i] = number
				x += len(number)
			elif col == '*':
				adj_matrix[y][x] = '*'
				x += 1
			else:
				x += 1
		y += 1


def search_rows(rows, y_idx, x_idx):
	global adj_matrix
	numbers = []
	y = y_idx
	for row in rows:
		x = x_idx
		for col in row[y_idx:y_idx+3]:
			print(x, y)
			if adj_matrix[y][x] != '0' and adj_matrix[y][x] != '*':
				numbers.append(adj_matrix[y][x])
			x += 1
		y += 1
	return list(set(numbers))



def search_matrix():
	global adj_matrix, data
	total_sum = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == '*':
				numbers = search_rows(data[max(0, y-1):min(y+2,len(data))], max(y - 1, 0), max(x - 1, 0))
				print(numbers)
				if len(numbers) == 2:
					total_sum += int(numbers[0]) * int(numbers[1])
	return total_sum


build_matrix()
print(search_matrix())

# Wrong   43045621
# too low 31980249
# too low 35312014
