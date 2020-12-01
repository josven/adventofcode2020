import itertools


with open("input.txt",'r') as file:
    all_lines = file.readlines()
    combinations = itertools.combinations(map(int, all_lines), 2)
    a, b = next(iter(filter(lambda (a, b) : a + b == 2020, combinations)))
    print(a * b)
