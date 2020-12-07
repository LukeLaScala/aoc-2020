lines = open('in').readlines()

part1 = 0
part2 = 0


def validate_year(x, start, end):
    try:
        int(x)
        return len(x) == 4 and start <= int(x) <= end
    except:
        return False


def validate_length(x):
    try:
        length = int(x[0:-2])
        if x[-2:] == "cm":
            return 150 <= length <= 193
        elif x[-2:] == "in":
            return 59 <= length <= 76

    except:
        return False

    return False


def validate_hair_color(x):
    if x[0] != "#":
        return False

    for char in x[1:]:
        if char not in "0123456789abcdef":
            return False

    return True


def validate_eye_color(x):
    return x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_passport_id(x):
    if len(x) != 9:
        return False
    print(x)
    for char in x:
        if char not in "0123456789":
            return False

    return True

def verify_kv(key, value):
    for field in FIELDS:
        if field[0] == key:
            return field[1](value)

    return True

FIELDS = [
    ("byr", lambda x: validate_year(x, 1920, 2002)),
    ("iyr", lambda x: validate_year(x, 2010, 2020)),
    ("eyr", lambda x: validate_year(x, 2020, 2030)),
    ("hgt", lambda x: validate_length(x)),
    ("hcl", lambda x: validate_hair_color(x)),
    ("ecl", lambda x: validate_eye_color(x)),
    ("pid", lambda x: validate_passport_id(x))
]

passports = []
passport = {}
for line in lines:
    if line == "\n":
        passports.append(passport)
        passport = {}
    else:
        for kv in line.split(' '):
            passport[kv.split(':')[0]] = kv.split(':')[1]

passports.append(passport)

for passport in passports:
    if all(key[0] in passport.keys() for key in FIELDS):
        part1 += 1
        print([verify_kv(key, passport[key].strip('\n')) for key in passport])
        if all([verify_kv(key, passport[key].strip('\n')) for key in passport]):
            part2 += 1

print("4a: ", part1)
print("4b: ", part2)