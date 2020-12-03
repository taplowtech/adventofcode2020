import helpers


def validate1(l):
    range = l.split(' ')[0]
    min = int(range.split('-')[0])
    max = int(range.split('-')[1])
    rest = l.split(' ', 1)[1]
    ch = rest.split(':')[0]
    p = rest.split(':', 1)[1].strip()
    # print(min, max, ch, p)
    c = p.count(ch)

    if c >= min and c <= max:
        return 1
    else:
        return 0


def validate2(l):
    range = l.split(' ')[0]
    min = int(range.split('-')[0])
    max = int(range.split('-')[1])
    rest = l.split(' ', 1)[1]
    ch = rest.split(':')[0]
    p = rest.split(':', 1)[1].strip()
    # print(min, max, ch, p)
    c = 0
    if p[min-1] == ch:
        c += 1
    if p[max-1] == ch:
        c += 1

    if c == 1:
        return 1
    else:
        return 0


test = helpers.read_file_as_array_str('./inputs_day2.txt')
valid = 0
for p in test:
    valid += validate1(p)

print('first part: ', valid)

valid = 0
for p in test:
    valid += validate2(p)

print('second part: ', valid)
