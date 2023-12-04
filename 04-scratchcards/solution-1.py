with open('input.txt') as f:
	data = f.readlines()


def split_cards(data: [str]) -> [([str], [str])]:
	"""
	Split the cards into pairs of winning and personal numbers.
	"""
	game_cards = []
	for row in data:
		row = row.split(':')[1].replace('\n', '')
		winning_str, personal_string = row.split('|')
		row_winning = list(filter(len, winning_str.split(' ')))
		row_personal = list(filter(len, personal_string.split(' ')))
		game_cards.append((row_winning, row_personal))
	return game_cards


def check_matches(winning:[str], personal:[str]) -> int:
	count = 0
	for card in personal:
		blacklist = []
		if card in winning:
			count += 1
	return count


def check_cards(cards: [([str], [str])]) -> int:
	total_sum = 0
	for row in cards:
		winning, personal = row
		count = check_matches(winning, personal)
		# To not calculate 2^-0.5
		if count > 0:
			total_sum += 2 ** (count - 1)
	return int(total_sum)


print(check_cards(split_cards(data)))