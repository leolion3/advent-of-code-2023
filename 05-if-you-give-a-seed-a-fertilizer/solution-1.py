import numpy as np
from typing import List, Dict
from scipy.optimize import minimize
from numba import njit

dicts = []

with open('input.txt') as f:
    data = f.read().replace('\n\n', '\n')
    seeds = np.array(list(map(int, data.split('seeds: ')[1].split('\n')[0].split(' '))))
    remainder = np.array(data.split('seeds: ')[1].split('\n')[1:])


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
                'values': np.array(values),
                'cache': []
            })
        i += 1


def get_next_seed(seed: int, ddicts: List[Dict]):
    if not len(ddicts):
        return seed
    next_dict = ddicts[0]
    values = next_dict['values']
    for value in values:
        target, src, drange = value
        if src <= seed <= src + drange:
            return get_next_seed(target + seed - src, ddicts[1:])
    return get_next_seed(seed, ddicts[1:])


def get_intervals(seed, mrange):
    global dicts
    intervals = np.array([(value[1], value[1] + value[2]) for value in dicts[0]['values']])

    start_range = np.maximum(intervals[:, 0], seed)
    end_range = np.minimum(intervals[:, 1], seed + mrange)

    seeds_within_range = np.concatenate([np.arange(start, end) for start, end in zip(start_range, end_range)])

    return seeds_within_range


def process_for_minimize(params):
    global dicts
    start_seed, drange = params
    new_seeds = get_intervals(int(start_seed), int(drange))

    locations = np.array([get_next_seed(int(seed), dicts) for seed in new_seeds])
    lowest = np.min(locations)

    return lowest


def sol_1(new_seeds):
    global dicts
    locations = np.array([get_next_seed(int(seed), dicts) for seed in new_seeds])
    return np.min(locations)


# NEVERMIND SOLUTION 2 with python.
def sol_2():
    global seeds, dicts
    lowest = np.inf
    for i in range(0, len(seeds), 2):
        print(f'Progress: {i}/{len(seeds)}', end='\r')
        bounds = [(0, None), (0, None)]
        result = minimize(process_for_minimize, x0=(seeds[i], seeds[i + 1]), bounds=bounds, method='powell')
        if result.fun < lowest:
            lowest = result.fun
    return lowest


create_dict()
print('Solution 1:', sol_1(seeds))
print('Solution 2:', sol_2())
