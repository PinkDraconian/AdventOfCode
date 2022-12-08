import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def get_view_distance(tree, looking_at):
    view_distance = 0
    for looking_at_tree in looking_at:
        if looking_at_tree < tree:
            view_distance += 1
        else:
            view_distance += 1
            break
    return view_distance


def main():
    grid = []
    for data in get_input('input/input.txt'):
        grid.append([int(i) for i in data])

    highest_scenic_score = 0
    height = len(grid)
    width = len(grid[0])
    visible_trees = height * 2 + width * 2 - 4
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            tree = grid[y][x]
            if len([tree2 for tree2 in grid[y][x+1:] if tree2 >= tree]) == 0 \
                    or len([tree2 for tree2 in grid[y][:x] if tree2 >= tree]) == 0 \
                    or len([tree2 for tree2 in [i[x] for i in grid[y+1:]] if tree2 >= tree]) == 0 \
                    or len([tree2 for tree2 in [i[x] for i in grid[:y]] if tree2 >= tree]) == 0:
                visible_trees += 1

            scenic_score = get_view_distance(tree, grid[y][x+1:]) \
                           * get_view_distance(tree, grid[y][:x][::-1]) \
                           * get_view_distance(tree, [i[x] for i in grid[y+1:]]) \
                           * get_view_distance(tree, [i[x] for i in grid[:y]][::-1])
            highest_scenic_score = max(scenic_score, highest_scenic_score)

    # Answer the first question: How many are visible
    answer(1, visible_trees)
    # Answer the second question: Highest scenic score
    answer(2, highest_scenic_score)


if __name__ == '__main__':
    main()
