import collections
import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


class SquareGrid:
    def __init__(self, height_map):
        self.height_map = height_map
        self.width = len(height_map[0])
        self.height = len(height_map)

    def get_height(self, node):
        x, y = node
        return self.height_map[y][x]

    def is_on_map(self, node):
        x, y = node
        return 0 <= x < self.width and 0 <= y < self.height

    def can_move(self, node1, node2):
        return self.get_height(node2) - self.get_height(node1) > 1

    def neighbors(self, node):
        x, y = node
        moves = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        neighbors = []
        for move in moves:
            if self.is_on_map(move):
                neighbors.append(move)
        return neighbors


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return not self.elements

    def add(self, element):
        self.elements.append(element)

    def get(self):
        return self.elements.popleft()


def breadth_first_search(grid, start, end):
    queue = Queue()
    queue.add(start)
    came_from = {start: None}
    steps = 0
    while not queue.empty():
        current_node = queue.get()
        if current_node == end:
            break
        for next_node in grid.neighbors(current_node):
            if next_node not in came_from and not grid.can_move(current_node, next_node):
                steps += 1
                came_from[next_node] = current_node
                queue.add(next_node)
    return came_from


def find_shortest_path(height_map, start, end):
    grid = SquareGrid(height_map)
    path = breadth_first_search(grid, start, end)
    node = end
    shortest_path = []
    while node != start:
        try:
            shortest_path.append(grid.get_height(path[node]))
            node = path[node]
        except KeyError:
            break
    return shortest_path


def find_shortest_climb_length(height_map, end):
    paths = []
    for y, row in enumerate(height_map):
        for x, height in enumerate(row):
            if height == ord('a'):
                paths.append(find_shortest_path(height_map, (x, y), end))
    return min([len(path) for path in paths if len(path) != 0])


def main():
    height_map = []
    start = ()
    end = ()
    for i, data in enumerate(get_input('input/input.txt')):
        height_map.append([])
        for j, letter in enumerate(data):
            if letter == 'S':
                start = (j, i)
                letter = 'a'
            elif letter == 'E':
                end = (j, i)
                letter = 'z'
            height_map[i].append(ord(letter))


    answer(1, len(find_shortest_path(height_map, start, end)))
    answer(2, find_shortest_climb_length(height_map, end))


if __name__ == '__main__':
    main()
