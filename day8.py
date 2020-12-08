import helpers


def dbgp(ins, state):
    # print(f'DBG> {ins=} {state=}')
    return


def ins_nop(state):
    global c

    state['pc'] += 1
    dbgp('nop', state)
    return state


def ins_acc(state):

    global c
    state['acc'] += int(c[state['pc']]['op1'])
    state['pc'] += 1
    dbgp('acc', state)
    return state


def ins_jmp(state):

    global c
    state['pc'] += int(c[state['pc']]['op1'])
    dbgp('jmp', state)
    return state


m = {
    'nop': ins_nop,
    'acc': ins_acc,
    'jmp': ins_jmp
}


c = []


def parse_code(c):

    p = []
    for l in c:
        xx = l.split(' ')
        if xx[0] not in m:
            print(f'invalid instruction {xx[0]}')
        else:
            ins = m[xx[0]]
            op1 = xx[1]
        p.append({'ins': ins, 'op1': op1})
    return p


def exec_statement_once(state):
    c[state['pc']]['visited'] += 1
    if c[state['pc']]['visited'] > 1:
        print(f'hit instruction more than once, acc was {state["acc"]}')
        state['abort'] = True
        return state
    else:
        state = c[state['pc']]['ins'](state)
    return state


def run_code_once():
    global c
    # mark if we've been here before
    for l in c:
        l['visited'] = 0
    state = {'pc': 0, 'acc': 0, 'abort': False, 'exit': False}
    while state['abort'] == False and state['exit'] == False:
        state = exec_statement_once(state)
        if state['pc'] == len(c):
            state['exit'] = True
    return state


test_data = helpers.read_file_as_array_str('inputs_test_day8.txt')
c = parse_code(test_data)
print(c)

test_res = run_code_once()

if test_res['acc'] != 5:
    print(f'algorithm part 1 not working...yet {test_res}')
    exit()

data = helpers.read_file_as_array_str('inputs_day8.txt')
c = parse_code(data)

res = run_code_once()
print(res)
print('part 1', res['acc'])

p = 0
exited = False
while not exited and p < len(c):
    print(f'{p=}')
    c = parse_code(helpers.read_file_as_array_str('inputs_day8.txt'))
    while p < len(c):
        if c[p]['ins'] == ins_nop:
            c[p]['ins'] = ins_jmp
            p += 1
            break
        if c[p]['ins'] == ins_jmp:

            c[p]['ins'] = ins_nop
            p += 1
            break
        p += 1
    res = run_code_once()
    if res['exit'] == True:
        print('part 2', res['acc'])
        exited = True
