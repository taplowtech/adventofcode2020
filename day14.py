import helpers


def combine_mask(mask, i):
    p = 35
    o = 0
    m = 1
    while p >= 0:
        v = i % 2
        i = int(i/2)
        if (v == 1 and mask[p] == 'X') or mask[p] == '1':
            o += m
        m = m*2
        p -= 1
    return o


def calc_sum(input):
    mem = {}
    for i in input:
        if 'mask' in i:
            mask = i.split(' = ')[1]
        elif 'mem' in i:
            v = int(i.split(' = ')[1])
            a = int(i.split('mem[', 1)[1].split(']', 1)[0])
            mem[a] = combine_mask(mask, v)
    s = 0
    for m in mem:
        s += mem[m]
    return s


def combine_mask2(mask, i):
    p = 35
    base = 0
    m = 1
    xpos = []
    while p >= 0:
        v = i % 2
        i = int(i/2)
        if mask[p] == 'X':
            xpos.append(m)
        else:
            if v == 1 or mask[p] == '1':
                base += m

        m = m*2
        p -= 1

    memlocs = []
    for a in range(0, pow(2, len(xpos))):
        p = 0
        m = base
        d = a
        while d > 0:
            if (d % 2):
                m += xpos[p]
            p += 1
            d = int(d/2)
        memlocs.append(m)
    return memlocs


def calc_sum2(input):
    mem = {}
    for i in input:
        if 'mask' in i:
            mask = i.split(' = ')[1]
        elif 'mem' in i:
            v = int(i.split(' = ')[1])
            a = int(i.split('mem[', 1)[1].split(']', 1)[0])
            for m in combine_mask2(mask, a):
                mem[m] = v
    s = 0
    for m in mem:
        s += mem[m]
    return s


test_inp = helpers.read_file_as_array_str(
    './inputs_test_day14.txt')
test_res = calc_sum(test_inp)
if test_res != 165:
    print(f'algorithm part 1 not working...yet')
    exit()


inp = helpers.read_file_as_array_str(
    './inputs_day14.txt')
res = calc_sum(inp)
print('part 1', res)

test_inp2 = helpers.read_file_as_array_str(
    './inputs_test_day14b.txt')
test_res2 = calc_sum2(test_inp2)
if test_res2 != 208:
    print(f'algorithm part 1 not working...yet')
    exit()

res = calc_sum2(inp)
print('part 2', res)
