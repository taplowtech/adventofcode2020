import helpers


def occ(map, x, y):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 0

    if map[y][x] == 'L' or map[y][x] == '.':
        return 0
    return 1


def occ_dir(map, x, y, ox, oy):
    x += ox
    y += oy
    while not (x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)):
        if map[y][x] == 'L':
            return 0
        if map[y][x] == '#':
            return 1
        x += ox
        y += oy
    return 0


def apply_rules(m):
    n = []

    for y in range(0, len(m)):
        r = ''

        for x in range(0, len(m[0])):
            o = occ(m, x-1, y-1)+occ(m, x-1, y)+occ(m, x-1, y+1)+occ(m, x, y-1) + \
                occ(m, x, y+1)+occ(m, x+1, y-1)+occ(m, x+1, y)+occ(m, x+1, y+1)
            if m[y][x] == 'L' and o == 0:
                r += '#'
            elif m[y][x] == '#' and o >= 4:
                r += 'L'
            else:
                r += m[y][x]
        n.append(r)

    return n


def apply_rules_2(m):
    n = []
    for y in range(0, len(m)):
        r = ''
        for x in range(0, len(m[0])):
            o = occ_dir(m, x, y, -1, -1)+occ_dir(m, x, y, 0, -1)+occ_dir(m, x, y, 1, -1) +\
                occ_dir(m, x, y, -1, 0)+occ_dir(m, x, y, 1, 0) +\
                occ_dir(m, x, y, -1, 1)+occ_dir(m, x, y, 0, 1) + \
                occ_dir(m, x, y, 1, 1)
            if m[y][x] == 'L' and o == 0:
                r += '#'
            elif m[y][x] == '#' and o >= 5:
                r += 'L'
            else:
                r += m[y][x]
        n.append(r)
    return n


def count_occupied(m):
    c = 0
    for y in range(0, len(m)):
        c += m[y].count('#')
    return c


def calc_steady_state(plan):
    c = count_occupied(plan)
    while True:
        plan = apply_rules(plan)
        new_c = count_occupied(plan)
        if new_c != c:
            c = new_c
        else:
            break
    return c


def show_plan(m):
    for y in m:
        print(y)
    print('------------------')


def calc_steady_state_2(plan):
    c = count_occupied(plan)
    while True:
        plan = apply_rules_2(plan)
        new_c = count_occupied(plan)
        if new_c != c:
            c = new_c
        else:
            break
    return c


test_inp = helpers.read_file_as_array_str(
    './inputs_test_day11.txt')
test_res = calc_steady_state(test_inp)

if test_res != 37:
    print(f'algorithm part 1 not working...yet')
    exit()

inp = helpers.read_file_as_array_str(
    './inputs_day11.txt')
res = calc_steady_state(inp)
print('part 1', res)

test_res = calc_steady_state_2(test_inp)
print(test_res)
if test_res != 26:
    print(f'algorithm part 2 not working...yet')
    exit()

inp = helpers.read_file_as_array_str(
    './inputs_day11.txt')
res = calc_steady_state_2(inp)
print('part 2', res)
