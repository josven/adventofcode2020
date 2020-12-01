import itertools


with open("input.txt",'r') as file:
    all_lines = file.readlines()
    combinations = itertools.combinations(map(int, all_lines), 3)
    a, b, c = next(iter(filter(lambda (a, b, c) : a + b + c == 2020, combinations)))
    print(a * b * c)
