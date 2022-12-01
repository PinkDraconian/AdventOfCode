def get_input(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()
