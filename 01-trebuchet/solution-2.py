#!/usr/bin/env python3

nums = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}


def check_digit(entry):
	return entry[0].isdigit()


def extract_number(entry):
	"""
	Check if the entry starts with a string number and replace it.
	:return: a number or an empty string and their length.
	"""
	global nums
	for str_val, val in nums.items():
		if entry.startswith(str_val):
			return val, len(str_val)
	return '', 0


def reformat_entry(entry):
	global nums
	new_entry = ''
	idx = 0
	while idx < len(entry):
		if check_digit(entry[idx]):
			new_entry += entry[idx]
		else:
			extracted, str_len = extract_number(entry[idx:])
			if str_len:
				new_entry += extracted
		idx += 1
	return new_entry



def get_code(entry):
	# Find first number
	first, last = None, None
	first = entry[0]
	last = (entry[::-1])[0]
	first = first or '0'
	last = last or '0'
	return ''.join([first, last])


with open('input.txt') as f:
	print(sum([int(get_code(reformat_entry(entry))) for entry in f.readlines()]))