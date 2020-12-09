import itertools
import math
import os
import re
from utils import time_this
from functools import partial
from itertools import starmap, product, permutations, combinations
from math import floor, ceil


PREAMBLE_LENGTH = 25


def find_invalid_number(data):
    for index, number in enumerate(data[PREAMBLE_LENGTH:]):
        preamble = data[index:PREAMBLE_LENGTH+index]
        sums = list(map(sum, combinations(preamble, 2)))
        if not number in sums:
            invalid_number = number
            return invalid_number


def find_weakness(invalid_number, data):
    for i1, start in enumerate(data, start=1):
        for i2, end in enumerate(data[i1:]):
            set_ = data[ data.index(start) : data.index(end) ]
            if sum(set_) == invalid_number:
                weakness = min(set_) + max(set_)
                return weakness
            if sum(set_) > invalid_number:
                break


@time_this
def solutions():
    file_name = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_name,'r') as file:
        data = file.read().splitlines()
        data = list(map(int, data))

    invalid_number = find_invalid_number(data)
    weakness = find_weakness(invalid_number, data)

    return invalid_number, weakness


print(solutions())
