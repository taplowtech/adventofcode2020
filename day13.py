import helpers
import time


def get_buses(l):
    return [int(bus) for bus in l.split(',') if bus != 'x']


def earliest_bus(now, buses):
    next_bus = None
    next_time = None
    for bus in buses:
        t = (int((now-1)/bus)+1)*bus

        if next_time == None or next_time > t:
            next_time = t
            next_bus = bus
    return (next_time-now)*next_bus


def earliest_time(i):
    o = 0
    buses = {}
    for b in i.split(','):
        if b != 'x':
            buses[int(b)] = o
        o += 1
    t = 0
    step = 1
    for bus in buses:
        bus_step = buses[bus]
        while (t+bus_step) % bus:
            t += step
        step = step*bus
    return t


test_inp = helpers.read_file_as_array_str(
    './inputs_test_day13.txt')
test_res = earliest_bus(int(test_inp[0]), get_buses(test_inp[1]))
if test_res != 295:
    print(f'algorithm part 1 not working...yet')
    exit()


inp = helpers.read_file_as_array_str(
    './inputs_day13.txt')
res = earliest_bus(int(inp[0]), get_buses(inp[1]))
print('part 1', res)

test_res = earliest_time(test_inp[1])
if test_res != 1068781:
    print(f'algorithm part 2 not working...yet')
    exit()
res = earliest_time(inp[1])
print('part 2', res)
