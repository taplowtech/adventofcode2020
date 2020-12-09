import helpers
import shared


def find_invalid(i, preamble_len):
    x = preamble_len+1
    while x < len(i):
        if not shared.find_pair_mul(i[x-preamble_len-1:x], i[x]):
            return i[x]
        x += 1


def find_list(i, t):
    for x in range(0, len(i)):
        y = x
        while y < len(i):
            if sum(i[x:y]) > t:
                break
            if sum(i[x:y]) == t:
                return min(i[x:y])+max(i[x:y])
            y += 1
    return None


test_inp = helpers.read_file_as_array_int('./inputs_test_day9.txt')
test_res = find_invalid(test_inp, 5)

if test_res != 127:
    print(f'algorithm part 1 not working...yet')
    exit()


inp = helpers.read_file_as_array_int('./inputs_day9.txt')
res1 = find_invalid(inp, 25)
print('part 1', res1)

if find_list(test_inp, test_res) != 62:
    print(f'algorithm part 2 not working...yet')
    exit()

res = find_list(inp, res1)
print('part 2', res)
