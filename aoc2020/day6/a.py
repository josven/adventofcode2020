import itertools
import math
import os
import re
from utils import time_this
from functools import partial
from math import floor, ceil
from itertools import combinations, product



@time_this
def solution():
    file_name = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_name,'r') as file:
        declaration_forms = file.read().split("\n\n")

    score = 0
    score_b = 0
    for i1, group in enumerate(declaration_forms, start=1):
        group_set = set()
        group_set_b = set()
        for i2, person in enumerate(group.split(), start=1):
            answers = set(person)
            group_set.update(answers)
            if i2 == 1:
                group_set_b.update(answers)
            else:
                group_set_b = group_set_b & answers
        score += len(group_set)
        score_b += len(group_set_b)
    return score, score_b


print(solution())
