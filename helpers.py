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
        res.append(f)
    return res
