#!/usr/bin/env python3
import string


forbidden = list(string.digits + '.\n') 


def get_vicinity(data, line_idx, number_idx, number):
	print('\nNumber:',number)
	prev_line = max(0, line_idx - 1)
	next_line = min(line_idx + 2, len(data))
	before_word = max(0, number_idx - 1)
	after_word = min(number_idx + len(number) + 1, len(data[line_idx]))
	elements = []
	for line in data[prev_line:next_line]:
		print(line[before_word:after_word])
		for entry in line[before_word:after_word]:
			elements += entry
	return elements


def check_validity(vicinity):
	global forbidden
	for c in vicinity:
		if c not in forbidden:
			return True
	return False



def get_number(line, idx):
	number = ''
	while line[idx].isdigit() and idx < len(line):
		number += line[idx]
		idx += 1
	return number


def get_valid_numbers(data):
	valid_numbers = []
	for line_idx in range(len(data)):
		line = data[line_idx]
		i = 0
		while i < len(line):
			if line[i].isdigit():
				number = get_number(line, i)
				if check_validity(get_vicinity(data, line_idx, i, number)):
					valid_numbers.append(number)
				i += len(number)
			else:
				i += 1
	return [int(i) for i in valid_numbers]



with open('input.txt', 'r') as f:
	data = f.readlines()
	print(sum(get_valid_numbers(data)))
