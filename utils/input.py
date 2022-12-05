def get_input(filename, do_strip=True):
    with open(filename) as file:
        for line in file:
            if do_strip:
                line = line.strip()
            yield line
