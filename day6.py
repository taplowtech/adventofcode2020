import helpers


def scan_customs_form_part1(f):
    form = set()
    filled = 0
    for r in f:
        if r == '':
            filled += len(form)
            form = set()
        else:
            for a in r:
                form.add(a)
    return filled


def count_customs_form(form, people):
    count = 0
    for a in form:
        if form[a] == people:
            count += 1
    return count


def scan_customs_form(f):
    form = {}
    people = 0
    filled = 0
    for r in f:

        if r == '':
            filled += count_customs_form(form, people)
            form = {}
            people = 0
        else:
            people += 1
            for a in r:
                if a not in form:
                    form[a] = 0
                form[a] += 1
    return filled


data = helpers.read_file_as_array_str('inputs_test_day6.txt')
test_res = scan_customs_form_part1(data)
if test_res != 11:
    print(f'algorithm part 1 not working...yet')
    exit()

data = helpers.read_file_as_array_str('inputs_day6.txt')
print('part 1:', scan_customs_form_part1(data))

data = helpers.read_file_as_array_str('inputs_test_day6.txt')
test_res = scan_customs_form(data)
if test_res != 6:
    print(f'algorithm for part 2 not working...yet, got {test_res}')
    exit()

data = helpers.read_file_as_array_str('inputs_day6.txt')
print('part 2:', scan_customs_form(data))
