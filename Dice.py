# %%
from fractions import Fraction
import itertools
import random
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
# %%
def count_combinations(list):
    return {key: value for key, value in sorted(Counter(map(sum, list)).items())}


def add_modifier(dict, mod=0):
    return {k+mod: dict[k] for k in dict }


def combinations(dict):
    dice_list = generate_list(dict)
    return list(itertools.product(*dice_list))


def generate_list(dict):
    list = []

    for key, value in dict.items():
        for n in range(1, value+1):
            list.append( [ *range(1, key+1) ] )

    return list


def dice_probabilities(dict, mod=0):
    return add_modifier(count_combinations(combinations(dict)), mod)
    
# %%
rolls = dice_probabilities({12:1,4:1}, 2)

print (rolls)

# %%
x = rolls.keys()

total_rolls = 0
for value in rolls.values():
    total_rolls += value

percent_rolls = [ n/total_rolls*100 for n in rolls.values()]

plt.bar(x, percent_rolls)
plt.show()