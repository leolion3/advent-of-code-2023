with open('input.txt') as f:
	game_times = list(map(int, list(filter(len, f.readlines(1)[0].rstrip().split(' ')))[1:]))
	game_distances = list(map(int, list(filter(len, f.readlines(1)[0].rstrip().split(' ')))[1:]))


def get_lowest_highest(record_time, record_distance):
	highest = -1
	lowest = -1
	# We need at least 1 second of movement 
	# and 1 less second than the record
	for t in range(0, record_time - 1)[::-1]:
		if record_time - t > record_distance:
			continue
		# dx = holding time (speed) * remaining_time
		dx = t * (record_time - t)
		if dx > record_distance:
			if highest == -1:
				highest = t
				lowest = t
			else:
				lowest = t
	return lowest, highest


def calc(game_times, game_distances):
	speeds = 1
	for i in range(len(game_times)):
		record_time = game_times[i]
		record_distance = game_distances[i]
		lowest, highest = get_lowest_highest(record_time, record_distance)	
		# Add 1 second to compensate for decrement.
		dlen = highest - lowest + 1
		if dlen == 0:
			continue
		speeds *= dlen
	return speeds


def sol_1():
	global game_times, game_distances
	print('Solution 1:', calc(game_times, game_distances))


def sol_2():
	global game_times, game_distances
	game_times = [int(''.join(list(map(str, game_times))))]
	game_distances = [int(''.join(list(map(str, game_distances))))]
	print('Solution 2:', calc(game_times, game_distances))
	


sol_1()
sol_2()