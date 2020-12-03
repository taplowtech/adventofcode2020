import helpers


def traverse(map, xi, yi):

    # xi and yi are increments, +x for right, +y for down and the opposite for the other two
    x = 0
    y = 0
    trees = 0
    while True:
        x = (x+xi) % (len(map[y]))
        y = y+yi
        if y >= len(map):
            break

        if map[y][x] == '#':
            trees += 1

    return trees


map = helpers.read_file_as_array_str(
    './inputs_day3.txt')

print(traverse(map, 3, 1))

rules = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
score = 1
for rule in rules:
    score = score * traverse(map, rule[0], rule[1])

print(score)
