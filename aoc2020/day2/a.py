import itertools
import time
import re

from ipdb import set_trace


pattern = "^(?P<min_>\d+)-(?P<max_>\d+)\s(?P<char>\S):\s(?P<password>\w+)"


def check(match):
    min_, max_, char, password = match
    counter = password.count(char)
    return int(min_)<= counter <= int(max_)


t0 = time.time()
with open("input.txt",'r') as file:
    all_lines = file.readlines()
    matches = map(lambda x: re.match(pattern, x).groups(), all_lines)
    ok_list = filter(check, matches)
    print(len(ok_list))
t1 = time.time()
print(t1 - t0)
