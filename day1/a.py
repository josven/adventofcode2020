import itertools


with open("input.txt",'r') as file:
    all_lines = file.readlines()
    combinations = itertools.combinations(map(int, all_lines), 2)
    for a, b in combinations:
        if a + b == 2020:
            print(a * b)

