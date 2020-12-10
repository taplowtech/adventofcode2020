import helpers
import shared


def calc_jolt_diff(i):
    i.sort()
    diff = [0, 0, 1]
    p = 0
    for a in i:
        if (a-p) > 3:
            print('difference too big')
            return None
        diff[a-p-1] += 1
        p = a
    return diff


def calc_jolt_comb(i):
    i.append(0)
    i.append(max(i)+3)
    maps = {}
    for a in i:
        maps[a] = 1
    i.sort()
    for a in range(len(i)-2, -1, -1):
        v = i[a]
        if (i[a+1]-v) >= 3:
            f = i[a+1]
            if f in maps:
                maps[v] = maps[f]
            else:
                maps[v] = 1
        else:
            maps[v] = 0
            x = a+1
            while (i[x]-v) <= 3:
                maps[v] += maps[i[x]]
                x += 1

    return maps[0]


test_inp_a = helpers.read_file_as_array_int('./inputs_test_day10a.txt')
test_res_a = calc_jolt_diff(test_inp_a)


if test_res_a != [7, 0, 5]:
    print(f'algorithm part 1a not working...yet')
    exit()


test_inp_b = helpers.read_file_as_array_int('./inputs_test_day10b.txt')
test_res_b = calc_jolt_diff(test_inp_b)


if test_res_b != [22, 0, 10]:
    print(f'algorithm part 1a not working...yet')
    exit()


inp_1 = helpers.read_file_as_array_int('./inputs_day10.txt')
res_1 = calc_jolt_diff(inp_1)

print('part 1', res_1[0]*res_1[2])


print('part 2', calc_jolt_comb(inp_1))
