import helpers


def parse(inp, lo, hi, min, max):
    for i in inp:
        if i == lo:
            max = int(((min+max+1)/2)-1)
        elif i == hi:
            min = int((min+max+1)/2)
    return min


data = helpers.read_file_as_array_str('inputs_day5.txt')

max_seatid = 0
seat_ids = []
for seat in data:
    row = parse(seat[0:7], 'F', 'B', 0, 127)
    col = parse(seat[7:], 'L', 'R', 0, 7)
    seatid = row*8+col
    if seatid > max_seatid:
        max_seatid = seatid
    seat_ids.append(seatid)
# part 1
print('part 1', max_seatid)

# part 2: your seat is the one where it isn't sequential:
seat_ids.sort()
for a in range(1, len(seat_ids)-1):
    if seat_ids[a]+1 != seat_ids[a+1]:
        print('part 2', seat_ids[a]+1)
