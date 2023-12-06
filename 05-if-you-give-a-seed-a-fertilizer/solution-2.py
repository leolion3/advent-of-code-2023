dicts = []

with open('input.txt') as f:
    data = f.read().replace('\n\n', '\n')
    seeds = list(map(int, data.split('seeds: ')[1].split('\n')[0].split(' ')))
    remainder = data.split('seeds: ')[1].split('\n')[1:]


def create_dict():
    global dicts, remainder
    i = 0
    while i < len(remainder):
        value = remainder[i]
        if 'map' in value:
            name, _ = value.split(' map:')
            values = []
            for j in range(i + 1, len(remainder) - 1):
                if 'map' in remainder[j]:
                    i = j - 1
                    break
                target, src, drange = map(int, remainder[j].split(' '))
                values.append((target, src, drange))
            dicts.append({
                'source': name.split('-')[0],
                'dest': name.split('-')[-1],
                'values': values
            })
        i += 1


def get_location_for_seed(seed: int):
    global dicts
    for ddict in dicts:
        for value in ddict['values']:
            target, src, drange = value
            if src <= seed < src + drange:
                seed = target + seed - src
                break
    return seed


# seed_start -> seed_start + range
# seed_start range
create_dict()


smallest = 10 ** 10

for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i+1]):
        val = get_location_for_seed(seed)
        if val < smallest:
            smallest = val
print(smallest)


