import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def display(cave):
    for i, row in enumerate(cave):
        print(str(i).ljust(2), ''.join(row))
    print()


def spawn_sand(cave, location):
    is_resting = False
    sand_location = [location, 0]
    while not is_resting:
        if cave[sand_location[1] + 1][sand_location[0]] == '.':
            sand_location = [sand_location[0], sand_location[1] + 1]
        elif cave[sand_location[1] + 1][sand_location[0] - 1] == '.':
            sand_location = [sand_location[0] - 1, sand_location[1] + 1]
        elif cave[sand_location[1] + 1][sand_location[0] + 1] == '.':
            sand_location = [sand_location[0] + 1, sand_location[1] + 1]
        else:
            is_resting = True
    if sand_location == [location, 0]: return 'Full!'
    cave[sand_location[1]][sand_location[0]] = 'o'
    if sand_location[1] == len(cave) - 2: return 'Flowing on the floor!'
    return 'Completed!'



def main():
    lines = []
    for line in get_input('input/input.txt'):
        lines.append([[int(part) for part in parts.split(',')] for parts in line.split(' -> ')])

    x = [part[0] for line in lines for part in line]
    y = [part[1] for line in lines for part in line]

    cave = []
    for i in range(max(y) + 1):
        cave.append(list('.' * (max(x) * 2)))
    cave.append(list('.' * (max(x) * 2)))
    cave.append(list('#' * (max(x) * 2)))

    for line in lines:
        previous_part = line[0]
        for part in line[1:]:
            for i in range(min(previous_part[0], part[0]), max(previous_part[0], part[0]) + 1):
                for j in range(min(previous_part[1], part[1]), max(previous_part[1], part[1]) + 1):
                    cave[j][i] = '#'
            previous_part = part

    sand_spawned = 0
    sand_spawned_until_flowing_on_floor = 0
    while True:
        sand_spawned += 1
        result = spawn_sand(cave, 500)
        if result == 'Full!':
            break
        elif result == 'Flowing on the floor!' and sand_spawned_until_flowing_on_floor == 0:
            sand_spawned_until_flowing_on_floor = sand_spawned - 1

    answer(1, sand_spawned_until_flowing_on_floor)
    answer(2, sand_spawned)


if __name__ == '__main__':
    main()
