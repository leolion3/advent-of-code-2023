#!/usr/bin/env python3


def check_minimum_cubes(dice_sets: [{str: int}]) -> bool:
	"""
	Checks the minimum amount of cubes required for a game.
	:param dice_sets: Dice color and their counts for each set.
	:return: red * green * blue for the minimum cube counts.
	"""
	colors = ['red', 'green', 'blue']
	counts = {color: 0 for color in colors}
	for dice_set in dice_sets:
		for color in colors:
			entry = dice_set.get(color)
			if entry is not None and entry > counts.get(color):
				counts[color] = entry
	mult = 1
	for color in colors:
		mult *= counts.get(color)
	return mult
	


def process_string(dice_set: [str]) -> {str: int}:
	"""
	Processes a given dice set and extracts the color counts.
	:param dice_set: Dice set like '3 blue, 4 red'
	:return: counts as { 'color': count, .. } dictionary
	"""
	counts = {}
	for color in ['red', 'green', 'blue']:
		for set_color in dice_set.split(','):
			if color in set_color:
				count = int(set_color.split(color)[0])
				counts[color] = count
	return counts


def check_set_possibility(game_id: str, game_data: [str]) -> int:
	"""
	Gets dice sets for every game and check if the games are possible.
	:param game_data: Dice sets for a game, like ['3 blue, 4 red', '1 red, 2 green, 6 blue'] 
	:return: The game id if the game is possible, or 0.
	"""
	possible = True
	counts = []
	for dice_set in game_data.split(';'):
		counts.append(process_string(dice_set))
	return check_minimum_cubes(counts)
	


def process_input(data):
	ids = []
	for entry in data:
		game_id, game_data = entry.split(':')
		ids.append(check_set_possibility(game_id, game_data))
	print(sum(ids))


with open('input.txt', 'r') as f:
	games = process_input(f.readlines())