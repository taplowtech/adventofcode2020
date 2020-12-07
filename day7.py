import helpers


def parse_luggage_rules(f):
    rules = {}
    for rule in f:
        outer = rule.split('contain')[0].replace('bags', '').strip()
        inner = rule.split('contain')[1].strip()[:-1]
        ii = {}
        if inner == 'no other bags':
            rules[outer] = None
        else:
            for i in inner.split(','):
                xx = i.strip().split(' ', 1)
                q = int(xx[0])
                b = xx[1]
                ii[b.replace('bags', '').replace(
                    'bag', '').strip()] = q
            rules[outer] = ii
    return rules


def count_bags_algo(bag_set, c, r):
    for a in r:
        rule = r[a]
        if rule != None:
            if c in rule:
                bag_set.add(a)
                bag_set = count_bags_algo(bag_set, a, r)
    return bag_set


def count_bags(c, r):
    return len(count_bags_algo(set(), c, r))


def count_inner(c, r):
    t = 0
    if r[c] == None:
        return 0
    for b in r[c]:
        x = count_inner(b, r)
        t += r[c][b]*(x+1)
    return t


test_data = helpers.read_file_as_array_str('inputs_test_day7.txt')
test_rules = parse_luggage_rules(test_data)
test_res = count_bags('shiny gold', test_rules)
if test_res != 4:
    print(f'algorithm part 1 not working...yet {test_res}')
    exit()

data = helpers.read_file_as_array_str('inputs_day7.txt')
rules = parse_luggage_rules(data)
print('part 1:', count_bags('shiny gold', rules))

test_res = count_inner('shiny gold', test_rules)

if test_res != 32:
    print(f'algorithm part 2 not working...yet {test_res}')
    exit()

print('part 2:', count_inner('shiny gold', rules))
