def get_lines(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line[:-1]


