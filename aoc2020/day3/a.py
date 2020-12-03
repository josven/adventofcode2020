import itertools
import math
import os

from utils import time_this


SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
FILE_NAME = os.path.join(os.path.dirname(__file__), 'input.txt')


def count_trees(slope,  map_):
    right, down = slope
    amount_rows = len(map_)
    rows = list(map(itertools.cycle, map_))
    step_right = iter(range(0, amount_rows * right, right))
    step_down = range(0, amount_rows, down)

    for i, row in enumerate(rows):
        [next(row) for step in range(next(step_right))]

    number_of_trees = 0
    for step in step_down:
        if next(rows[step]) == "#":
            number_of_trees += 1

    return number_of_trees


with open(FILE_NAME,'r') as file:
    map_ = file.read().splitlines()

@time_this
def first_slope():
    first_slope = count_trees(SLOPES[1], map_)
    print(first_slope)

@time_this
def all_slopes():
    all_slopes = math.prod(map(lambda slope: count_trees(slope, map_), SLOPES))
    print(all_slopes)


first_slope()
all_slopes()