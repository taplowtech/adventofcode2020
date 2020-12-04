def read_file_as_array_int(filename):
    f = open(filename, 'r')
    res = []
    for f in f.readlines():
        res.append(int(f))
    return res


def read_file_as_array_str(filename):
    f = open(filename, 'r')
    res = []
    for f in f.readlines():
        res.append(f.replace('\n', ''))
    return res

def validate_year(i, min, max):
    try:
        year = int(i)
        if (year >= min) and (year <= max):
            return True
    except:
        return False
    return False


def validate_chars(i, valid, vlen):
    if len(i) != vlen:
        return False
    for c in i:
        if c not in valid:
            return False
    return True
