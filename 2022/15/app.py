import re
import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


sensors = []
beacons = []
closest_distances = []


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def can_beacon_be_here(x, y):
    global sensors, closest_distances
    for i, sensor in enumerate(sensors):
        if manhattan_distance([x, y], sensor) <= closest_distances[i] and [x, y] not in beacons:
            return sensor[0] + closest_distances[i] - abs(y - sensor[1])
    return 'Yes!'

def main():
    global sensors, closest_distances, beacons
    for data in get_input('input/input.txt'):
        matches = re.findall(r'x=(-?\d*), y=(-?\d*)', data)
        matches = [int(data) for match in matches for data in match]
        sensors.append(matches[:2])
        beacons.append(matches[2::])
        closest_distances.append(manhattan_distance(matches[:2], matches[2::]))
    beacons = [list(y) for y in set([tuple(x) for x in beacons])]

    y = 2000000
    impossible_locations = 0
    sensor_x_min = min([sensor[0] - closest_distances[i] for i, sensor in enumerate(sensors)])
    sensor_x_max = max([sensor[0] + closest_distances[i] for i, sensor in enumerate(sensors)])
    x = sensor_x_min
    while x < sensor_x_max + 1:
        result = can_beacon_be_here(x, y)
        if result != 'Yes!':
            impossible_locations += result - x + 1
            x = result
        x += 1
    answer(1, impossible_locations - len([beacon for beacon in beacons if beacon[1] == y]))

    for y in range(0, 4000001):
        x = 0
        while x < 4000001:
            result = can_beacon_be_here(x, y)
            if result == 'Yes!' and [x, y] not in beacons:
                answer(2, x * 4000000 + y)
                return
            else:
                x = result
            x += 1


if __name__ == '__main__':
    main()
