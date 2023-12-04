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
		if card in winning:
			count += 1
	return count


def check_cards(cards: [([str], [str])], idx: int, lastidx: int) -> int:
	"""
	Recursively check card stack for card matches.
	:return: the amount of cards held.
	"""
	total_cards = 0
	for row_id in range(idx, lastidx):
		total_cards += 1
		winning, personal = cards[row_id]
		count = check_matches(winning, personal)
		if count > 0:
			total_cards += check_cards(cards, row_id + 1, row_id + count + 1)
	return total_cards


total_sum = 0
for i in range(len(data)):
	total_sum += check_cards(split_cards(data), i, i + 1)
print(total_sum)