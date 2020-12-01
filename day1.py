import helpers


def find_pair(input, total):
    match = []
    for i in input:
        if i in match:
            return i*(total-i)
        else:
            match.append(total-i)
    return None


def find_triple(input, total):
    for i in input:
        copy = input.copy()
        copy.remove(i)
        r = find_pair(copy, total-i)
        if r != None:
            return i*r
    return None


print(find_pair(helpers.read_file_as_array_int('./inputs_day1.txt'), 2020))
print(find_triple(helpers.read_file_as_array_int('./inputs_day1.txt'), 2020))
