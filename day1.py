import helpers
import shared


def find_triple(input, total):
    for i in input:
        copy = input.copy()
        copy.remove(i)
        r = shared.find_pair_mul(copy, total-i)
        if r != None:
            return i*r
    return None


print(shared.find_pair_mul(helpers.read_file_as_array_int('./inputs_day1.txt'), 2020))
print(find_triple(helpers.read_file_as_array_int('./inputs_day1.txt'), 2020))
