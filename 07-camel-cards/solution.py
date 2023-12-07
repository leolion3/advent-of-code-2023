#!/usr/bin/env python3
# Ugly but I was too lazy, feel free to optimize
import sys
if len(sys.argv) < 2:
	print(f'Usage {sys.argv[0]} data_file')
	exit(-1)
file = sys.argv[1]

hands = {}
card_vals = {
	'A': 14,
	'K': 13,
	'Q': 12,
	'J': 11,
	'T': 10,
	'9': 9,
	'8': 8,
	'7': 7,
	'6': 6,
	'5': 5,
	'4': 4,
	'3': 3,
	'2': 2
}


with open(file) as f:
	for line in f.readlines():
		if not len(line):
			break
		hand, bid = line.rstrip().split(" ")
		hands[hand] = bid


def compare(card, next_card):
	global card_vals
	for c in range(len(card)):
		if card_vals.get(card[c]) > card_vals.get(next_card[c]):
			return True
		elif card_vals.get(card[c]) < card_vals.get(next_card[c]):
			return False
	return False


def sort_cards(cards) -> []:
	n = len(cards)
	for _ in range(n):
		for j in range(1, n):
			if compare(cards[j-1], cards[j]):
				cards[j], cards[j-1] = cards[j-1], cards[j]
	return cards


def get_sum(cards):
	global hands
	total_sum = 0
	for i in range(len(cards)):
		card = cards[i]
		bid = hands.get(card)
		total_sum += int(bid) * (i + 1)
	return total_sum


def sum_sort(lists):
	fives, fours, full_h, threes, twos, ones, high = lists
	sorted_fives = sort_cards(fives)
	sorted_fours = sort_cards(fours)
	sorted_full_h = sort_cards(full_h)
	sorted_threes = sort_cards(threes)
	sorted_twos = sort_cards(twos)
	sorted_ones = sort_cards(ones)
	sorted_high = sort_cards(high)
	result = (
		sorted_high + 
		sorted_ones +
		sorted_twos +
		sorted_threes +
		sorted_full_h +
		sorted_fours +
		sorted_fives
	)
	return get_sum(result)


def get_lists():
	global hands
	fives = []
	fours = []
	full_h = []
	threes = []
	twos = []
	ones = []
	high = []
	for hand in hands.keys():
		unique = len(set(list(hand)))
		# Five of a kind
		if unique == 5:
			high.append(hand)
		# One pair
		elif unique == 4:
			ones.append(hand)
		# Two pair or three of a kind
		elif unique == 3:
			counts = [hand.count(s) for s in hand]
			if counts.count(3) >= 1:
				threes.append(hand)
			else:
				twos.append(hand)
		elif unique == 1:
			fives.append(hand)
		elif unique == 2:
			c = hand.count(hand[0])
			# Four of a kind
			if c == 1 or c == 4:
				fours.append(hand)
			# Full house
			else:
				full_h.append(hand)
		else:
			'Undecided:', hand
	return fives, fours, full_h, threes, twos, ones, high


def get_joker_lists():
	global hands, card_vals
	card_vals['J'] = 1
	fives = []
	fours = []
	full_h = []
	threes = []
	twos = []
	ones = []
	high = []
	for hand in hands.keys():
		if 'J' in hand:
			unique = len(set(list(hand.replace('J', ''))))
			j_count = hand.count('J')
			if j_count >= 3:
				if unique <= 1:
					fives.append(hand)
				else:
					fours.append(hand)
			elif j_count == 2:
				if unique == 1:
					fives.append(hand)
				elif unique == 2:
					fours.append(hand)
				else:
					threes.append(hand)
			else:
				if unique == 1:
					fives.append(hand)
				elif unique == 2:
					counts = [hand.count(s) for s in hand.replace('J', '')]
					if 3 in counts:
						fours.append(hand)
					else:
						full_h.append(hand)
				elif unique == 3:
					threes.append(hand)
				else:
					ones.append(hand)
		else:
			unique = len(set(list(hand)))
			if unique == 5:
				high.append(hand)
			# One pair
			elif unique == 4:
				ones.append(hand)
			# Two pair or three of a kind
			elif unique == 3:
				counts = [hand.count(s) for s in hand]
				if counts.count(3) >= 1:
					threes.append(hand)
				else:
					twos.append(hand)
			elif unique == 1:
				fives.append(hand)
			elif unique == 2:
				c = hand.count(hand[0])
				# Four of a kind
				if c == 1 or c == 4:
					fours.append(hand)
				# Full house
				else:
					full_h.append(hand)
	return fives, fours, full_h, threes, twos, ones, high


def sol_1():
	return sum_sort(get_lists())

def sol_2():
	global card_vals
	card_vals['J'] = 0
	return sum_sort(get_joker_lists())

print("Solution 1:", sol_1())
print("Solution 2:", sol_2())