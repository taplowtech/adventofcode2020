def find_pair_mul(input, total):
    match = []
    for i in input:
        if i in match:
            return i*(total-i)
        else:
            match.append(total-i)
    return None
