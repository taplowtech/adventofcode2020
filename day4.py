import helpers


def valid_byr(i):
    return helpers.validate_year(i, 1920, 2002)


def valid_iyr(i):
    return helpers.validate_year(i, 2010, 2020)


def valid_eyr(i):
    return helpers.validate_year(i, 2020, 2030)


def valid_hgt(i):
    if i[-2:] == 'cm':
        try:
            height = int(i[:-2])
            print(height)
            if (height >= 150) and (height <= 193):
                return True
        except:
            return False
    if i[-2:] == 'in':
        try:
            height = int(i[:-2])
            print(height)
            if (height >= 59) and (height <= 76):
                return True
        except:
            return False
    return False


def valid_hcl(i):
    valid = '0123456789abcdef'
    if i[0] != '#':
        return False
    return helpers.validate_chars(i[1:7], '0123456789abcdef', 6)


def valid_ecl(i):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if i in valid:
        return True
    return False


def valid_pid(i):
    return helpers.validate_chars(i, '0123456789', 9)


mandatory = {'byr': valid_byr, 'iyr': valid_iyr, 'eyr': valid_eyr,
             'hgt': valid_hgt, 'hcl': valid_hcl, 'ecl': valid_ecl, 'pid': valid_pid}


def check_passport(passport):

    for m in mandatory:
        if m not in passport:
            return False

    return True


def validate_passport(passport):
    for m in mandatory:
        if m not in passport:
            return False
        a = mandatory[m](passport[m].replace('\n', ''))

        if a == False:
            return False
    return True


data = helpers.read_file_as_array_str('inputs_day4.txt')

passport = {}
valid = 0
validated = 0
for l in data:
    if l == '':
        if check_passport(passport):
            valid += 1
        if validate_passport(passport):
            validated += 1
        passport = {}
    else:
        d = l.split()
        for k in d:
            passport[k.split(':')[0]] = k.split(':')[1]
print('Part 1:', valid)
print('Part 2:', validated)
