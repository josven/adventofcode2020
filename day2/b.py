import itertools
import time
import re
import operator


pattern = "^(?P<first_position>\d+)-(?P<second_position>\d+)\s(?P<char>\S):\s(?P<password>\w+)"


def checks(match):
    
    first_position, second_position, char, password = match

    def check_length():
        return len(password) >= int(first_position)

    def check_position(pos):
        return password[int(pos) - 1] == char

    return check_length() and (check_position(first_position) ^ check_position(second_position))


t0 = time.time()
with open("input.txt",'r') as file:
    all_lines = file.readlines()
    matches = map(lambda x: re.match(pattern, x).groups(), all_lines)
    ok_list = filter(checks, matches)
    print(len(ok_list))
t1 = time.time()
print(t1 - t0)
