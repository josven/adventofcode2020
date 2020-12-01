import itertools


with open("input.txt",'r') as file:
    all_lines = file.readlines()
    combinations = itertools.combinations(map(int, all_lines), 3)
    for a, b, c in combinations:
        if a + b + c == 2020:
            print(a * b * c)

