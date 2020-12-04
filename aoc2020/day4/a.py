import itertools
import math
import os
import re
from utils import time_this
from functools import partial


def is_valid(passport, check_values=False):

    eye_colors = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]

    def check_hgt(hgt):
        constraints = {
            "cm": lambda heigth: 150 <= int(heigth) <= 193,
            "in": lambda heigth: 59 <= int(heigth) <= 76,
        }
        match = re.match("^(?P<heigth>\d+)(?P<unit>cm|in)$", hgt)
        if match:
            heigth, unit = match.groups()
            return constraints[unit](heigth)
        return False

    def has_mandatory_fields(passport):
        valid_fields = set(field_checks.keys())
        passport_fields = set(passport.keys())
        return valid_fields.issubset(passport_fields)

    def has_valid_values(passport):
        for field_name, check in field_checks.items():
            if not check(passport[field_name]):
                return False
        return True

    field_checks = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": check_hgt,
        "hcl": lambda x: re.match("^#(?:[0-9a-f]{6})$", x),
        "ecl": lambda x: x in eye_colors,
        "pid": lambda x: re.match("^\d{9}$", x),
        # "cid": "(Country ID) not used",
    }
    
    has_valid_fields = has_mandatory_fields(passport)
    if check_values:
        return has_valid_fields and has_valid_values(passport)
    return has_valid_fields


def load_passports(data_file='input.txt'):
    file_name = os.path.join(os.path.dirname(__file__), data_file)
    with open(file_name,'r') as file:
        data = file.read().split("\n\n")
    return [{
        fields.split(":")[0]: fields.split(":")[1]
        for fields in passport.split()
    } for passport in data]


@time_this
def part_one():
    passports = load_passports()
    valid_passports = list(filter(partial(is_valid, check_values=False), passports))
    print(len(valid_passports))


@time_this
def part_two():
    passports = load_passports()
    valid_passports = list(filter(partial(is_valid, check_values=True), passports))
    print(len(valid_passports))


part_one()
part_two()
