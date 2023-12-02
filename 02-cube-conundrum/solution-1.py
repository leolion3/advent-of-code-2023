#!/usr/bin/env python3

cubes = {
	'red': 12,
	'green': 13,
	'blue': 14
}


def check_possible_game(dice_count: {str: int}) -> bool:
	"""
	Checks if a given dice combination is possible.
	:param dice_count: Dice color and their counts.
	:return: true if the game is possible, and false otherwise.
	"""
	global cubes
	for color, count in dice_count.items():
		if count > cubes.get(color):
			return False
	return True


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
	for dice_set in game_data.split(';'):
		possible = check_possible_game(process_string(dice_set))
		if not possible:
			return 0
	return int(game_id.split('Game ')[1])


def process_input(data):
	ids = []
	for entry in data:
		game_id, game_data = entry.split(':')
		ids.append(check_set_possibility(game_id, game_data))
	print(sum(ids))


with open('input.txt', 'r') as f:
	games = process_input(f.readlines())