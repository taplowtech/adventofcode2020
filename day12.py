import helpers
import math


def rotate(x, y, r):
    rad = math.radians(r)
    return x*math.cos(rad)+y*math.sin(rad), y*math.cos(rad)-x*math.sin(rad)


def move_ferry(m):
    x = 0
    y = 0
    h_x = 1
    h_y = 0
    for r in m:
        a = r[0]
        d = int(r[1:])
        if a == 'N':
            y += d
        elif a == 'S':
            y -= d
        elif a == 'E':
            x += d
        elif a == 'W':
            x -= d
        elif a == 'L':
            h_x, h_y = rotate(h_x, h_y, -d)
        elif a == 'R':
            h_x, h_y = rotate(h_x, h_y, d)
        elif a == 'F':
            x += d*h_x
            y += d*h_y

    return int(abs(x)+abs(y))


def move_ferry_waypoint(m):
    x = 10
    y = 1
    ferry_x = 0
    ferry_y = 0
    h = [1, 0]
    for r in m:
        a = r[0]
        d = int(r[1:])
        if a == 'N':
            y += d
        elif a == 'S':
            y -= d
        elif a == 'E':
            x += d
        elif a == 'W':
            x -= d
        elif a == 'L':
            x, y = rotate(x, y, -d)
        elif a == 'R':
            x, y = rotate(x, y, d)
        elif a == 'F':
            ferry_x += d*x
            ferry_y += d*y
    return int(abs(ferry_x)+abs(ferry_y))


test_inp = helpers.read_file_as_array_str(
    './inputs_test_day12.txt')
test_res = move_ferry(test_inp)
print(test_res)
if test_res != 25:
    print(f'algorithm part 1 not working...yet')
    exit()


inp = helpers.read_file_as_array_str(
    './inputs_day12.txt')
res = move_ferry(inp)
print('part 1', res)


test_res = move_ferry_waypoint(test_inp)
print(test_res)
if test_res != 286:
    print(f'algorithm part 2 not working...yet')
    exit()

res = move_ferry_waypoint(inp)
print('part 2', res)
