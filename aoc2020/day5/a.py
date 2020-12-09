import itertools
import math
import os
import re
from utils import time_this
from functools import partial
from math import floor, ceil
from itertools import combinations, product


def load_boarding_passes(data_file='input.txt'):
    file_name = os.path.join(os.path.dirname(__file__), data_file)
    with open(file_name,'r') as file:
        data = file.read().split("\n\n")
    return [{
        fields.split(":")[0]: fields.split(":")[1]
        for fields in passport.split()
    } for passport in data]


@time_this
def part_one():

    file_name = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_name,'r') as file:
        boarding_passes = file.read().splitlines()

    row_ids = map((8).__mul__, range(0, 128))
    row_ids_and_seat_ids = list(product(row_ids, list(range(0, 8))))
    all_ids = list(map(sum, row_ids_and_seat_ids))
    ids = []
    for boarding_pass in boarding_passes:
        rows = list(range(0, 128))
        for half in boarding_pass[:7]:
            h = int(len(rows) / 2)
            if half == "B":
                rows = rows[h:]
            if half == "F":
                rows = rows[:h]

        seats = list(range(0, 8))
        for col in boarding_pass[7:]:
            h = int(len(seats) / 2)
            if col == "R":
                seats = seats[h:]
            if col == "L":
                seats = seats[:h]
        
        seat_id = (rows[0] * 8) + seats[0]
        ids.append(seat_id)
        all_ids.remove(seat_id)

    return max(ids), all_ids


print(part_one())
